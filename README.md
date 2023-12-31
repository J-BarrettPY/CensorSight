# CensorSight - Python Scripts

CensorSight is a collection of Python scripts that leverage computer vision techniques to provide various levels of privacy by censoring or blurring faces in a real-time webcam feed. These scripts use the popular computer vision library OpenCV and the dlib library for face detection and facial landmark prediction.

You MUST download "Face Landmarks" release and place shape_predictor_68_face_landmarks.dat in the same directory!

## Table of Contents

1. [Introduction](#introduction)
2. [Dependencies](#dependencies)
3. [Scripts](#scripts)
    - [censorsight-eyeblock.py](#censorsight-eyeblockpy)
    - [censorsight-faceblur.py](#censorsight-faceblurpy)
    - [censorsight-noface-blur.py](#censorsight-noface-blurpy)

## Introduction <a name="introduction"></a>

In today's world, privacy is of paramount importance. CensorSight scripts provide an interesting and practical solution to address privacy concerns in a fun and educational way. These scripts offer three different methods to censor faces in real-time webcam footage:

1. **censorsight-eyeblock.py**: This script detects faces and censors the eyes using a black rectangle. It is a humorous way to obscure the eyes while leaving the rest of the face visible.

2. **censorsight-faceblur.py**: This script detects faces and applies a Gaussian blur to the entire face region, effectively anonymizing individuals in the video stream.

3. **censorsight-noface-blur.py**: This script blurs the entire video frame when no faces are detected, preserving privacy by default and only applying blurring when necessary.

## Dependencies <a name="dependencies"></a>

Before running any of the CensorSight scripts, you need to install the following dependencies:

- Python 3.x
- OpenCV (`cv2`)
- dlib
- "shape_predictor_68_face_landmarks.dat" - You need to download this facial landmarks model file separately.

You can install OpenCV and dlib using pip:

```bash
pip install opencv-python
pip install dlib
```

Make sure to place the "shape_predictor_68_face_landmarks.dat" file in the same directory as the scripts.

## Scripts <a name="scripts"></a>

### censorsight-eyeblock.py <a name="censorsight-eyeblockpy"></a>

This script detects faces in the webcam feed and censors the eyes using a black rectangle. It's a playful approach to privacy protection, obscuring the eyes while keeping the rest of the face visible.

### censorsight-faceblur.py <a name="censorsight-faceblurpy"></a>

This script detects faces in the webcam feed and applies a Gaussian blur to the entire face region. It provides a more conventional way to anonymize individuals in real-time video.

### censorsight-noface-blur.py <a name="censorsight-noface-blurpy"></a>

This script continuously captures video from the webcam and applies a Gaussian blur to the entire frame if no faces are detected. It offers a simple way to maintain privacy by default and only blur the video when necessary.

To run any of these scripts, simply execute them using Python. Press 'q' to exit the program when you're done.
