import cv2
import numpy as np
import time

def create_background(cap, num_frames=30):
    print("Capturing background. Please move out of frame.")
    backgrounds = []
    
    for i in range(num_frames):
        ret, frame = cap.read()
        if ret:
            frame = np.flip(frame, axis=1)  # Mirror effect
            backgrounds.append(frame)
        else:
            print(f"Warning: Could not read frame {i+1}/{num_frames}")
        time.sleep(0.1)

    if len(backgrounds) > 0:
        return np.median(backgrounds, axis=0).astype(np.uint8)
    else:
        raise ValueError("Could not capture any frames for background")


def create_mask(frame, lower_color, upper_color):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Noise removal
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel, iterations=1)

    return mask


def apply_cloak_effect(frame, mask, background):
    mask_inv = cv2.bitwise_not(mask)

    fg = cv2.bitwise_and(frame, frame, mask=mask_inv)
    bg = cv2.bitwise_and(background, background, mask=mask)

    return cv2.add(fg, bg)


def main():
    print("OpenCV version:", cv2.__version__)

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Allow camera to warm up
    time.sleep(2)

    try:
        background = create_background(cap)
    except ValueError as e:
        print(f"Error: {e}")
        cap.release()
        return

    # HSV range for sky blue (adjust if needed)
    lower_sky_blue = np.array([90, 50, 50])
    upper_sky_blue = np.array([130, 255, 255])

    print("Starting main loop. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame.")
            time.sleep(1)
            continue

        frame = np.flip(frame, axis=1)  # Mirror frame

        mask = create_mask(frame, lower_sky_blue, upper_sky_blue)
        result = apply_cloak_effect(frame, mask, background)

        cv2.imshow('Invisible Cloak', result)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
