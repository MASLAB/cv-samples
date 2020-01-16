# MASLAB 2020 CV Lecture Example Code
This repo contains example code used in the demos for the MASLAB 2020 CV lecture.

Slides [here](https://docs.google.com/presentation/d/1SSGMEjHwkinFj3I0PVrSh51hBfSTtkA3sM__b9zMBVc/edit?usp=sharing).

Regular Github mirror for easy cloning onto NUC: https://github.com/nmoroze/cv-examples

## Setting up
To run this code, you'll need a webcam built into or attached to your computer,
and the OpenCV and AprilTags Python packages installed.

```
pip install opencv-python apriltag
```

Be sure to set the correct value for `CAMERA_INDEX` in each file before you run it
(this may take some trial-and-error).

## Running
Both demos can be run directly: `python color_segmentation.py` or `python apriltag_tracking.py`. They both open up windows displaying annotated output, and can be exited when the window is in focus by pressing `q`.

