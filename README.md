# Face Blur Using OpenCV

This project uses OpenCV to detect and blur faces in real-time using a webcam.

## Prerequisites
- Python 3.12
- OpenCV
- NumPy

## Installation

1. **Install NumPy**
   Run the following command to install or reinstall NumPy:
   ```bash
   "C:\Program Files\Python312\python.exe" -m pip install --force-reinstall numpy
   ```

2. **Install OpenCV**
   Run the following command to install or reinstall OpenCV:
   ```bash
   "C:\Program Files\Python312\python.exe" -m pip install --force-reinstall opencv-python
   ```

3. **Download Haar Cascade File**
   Download the face detection model (haarcascade_frontalface_default.xml) from the following link:
   - [Haarcascade Frontalface XML](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)

   Save it to the same directory as your `faceblur.py` file.

## Running the Program

1. Open a terminal or command prompt.
2. Navigate to the directory where `faceblur.py` is located.
3. Run the following command:
   ```bash
   "C:\Program Files\Python312\python.exe" faceblur.py
   ```

## Exiting the Program
- Press **`t`** to exit the application.

## Troubleshooting
- Ensure the `haarcascade_frontalface_default.xml` file is in the correct directory.
- Confirm OpenCV is installed by running:
  ```bash
  "C:\Program Files\Python312\python.exe" -c "import cv2; print(cv2.__version__)"
  ```
- Check if the correct Python version is used by running:
  ```bash
  where python
  ```
