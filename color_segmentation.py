# Simple color segmentation demo/example code for MASLAB 2020 CV Lecture

import sys
import cv2
import numpy as np

# CAMERA_INDEX indicates which webcam to use if we have
# multiple connected. If you just have one, use '0'.
CAMERA_INDEX = 0

# cap is a VideoCapture object we can use to get frames from webcam
cap = cv2.VideoCapture(CAMERA_INDEX)

# Min and max HSV thresholds for green
GREEN_THRESHOLD = ([70,50,50], [90,255,255])

while True:
  # Capture a frame from the webcam
  _, frame = cap.read()

  # Convert BGR to HSV
  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

  # OpenCV needs bounds as numpy arrays
  lower_bound = np.array(GREEN_THRESHOLD[0])
  upper_bound = np.array(GREEN_THRESHOLD[1])

  # Threshold the HSV image to get only green color
  # Mask contains a white on black image, where white pixels
  # represent that a value was within our green threshold.
  mask = cv2.inRange(hsv, lower_bound, upper_bound)

  # Find contours (distinct edges between two colors) in mask using OpenCV builtin
  # This function returns 2 values, but we only care about the first

  # Note: In some OpenCV versions this function will return 3 values, in which
  # case the second is the contours value. If you have one of those versions of
  # OpenCV, you will get an error about "unpacking values" from this line, which you
  # can fix by adding a throwaway variable before contours
  contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

  # If we have contours...
  if len(contours) != 0:
    # Find the biggest countour by area
    c = max(contours, key = cv2.contourArea)

    # Get a bounding rectangle around that contour
    x,y,w,h = cv2.boundingRect(c)

    # Draw the rectangle on our frame
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

  # Display that frame (resized to be smaller for convenience)
  cv2.imshow('frame', cv2.resize(frame, (1280, 720)))

  # Quit if user presses q
  if cv2.waitKey(1) & 0xFF == ord('q'):
      break
