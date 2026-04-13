#  Invisible Cloak using OpenCV (Python)

A fun Computer Vision project that creates a real-time **invisibility cloak effect** using Python and OpenCV — just like in Harry Potter!

---

##  Project Overview

This project uses **color detection and image processing** to replace a specific colored object (like a blue cloth) with the background, making it appear invisible.

---

##  Features

*  Real-time video processing
*  Color-based object detection (HSV masking)
*  Background subtraction using median filtering
*  Smooth cloak effect with noise reduction
*  Live camera feed with instant output

---

##  Technologies Used

* Python 
* OpenCV (`cv2`)
* NumPy
* Computer Vision concepts

---

##  How It Works

1. Capture background frames when the object is not present
2. Detect cloak color using HSV color space
3. Create a mask for the selected color
4. Replace cloak area with background
5. Display the final invisibility effect

---

##  Installation

```bash
git clone https://github.com/your-username/invisible-cloak-opencv.git
cd invisible-cloak-opencv
pip install opencv-python numpy
```

---

##  Usage

```bash
python main.py
```

* Stay out of frame for a few seconds (background capture)
* Use a **blue cloth/object**
* Press **'q'** to exit

---

##  Configuration

You can change cloak color by modifying HSV values:

```python
lower_sky_blue = np.array([90, 50, 50])
upper_sky_blue = np.array([130, 255, 255])
```

---

##  Requirements

* Webcam 
* Good lighting conditions 
* Background without similar colors
