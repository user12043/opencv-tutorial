#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# created by user12043 on 31.07.2021 - 18:43
# part of project opencv-tutorial

import cv2 as cv
import numpy as np

# For HSV, hue range is [0,179], saturation range is [0,255], and value range is [0,255]. Different software use
# different scales. So if you are comparing OpenCV values with them, you need to normalize these ranges.

cap = cv.VideoCapture(0)
while (1):
    # Take each frame
    _, frame = cap.read()

    # Resize if big
    if frame.shape[:2] > (360, 480):
        frame = cv.resize(frame, (480, 360), interpolation=cv.INTER_AREA)

    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    # define range of green color in HSV
    lower_green = np.array([50, 50, 50])
    upper_green = np.array([70, 255, 255])
    # define range of red color in HSV
    lower_red = np.array([170, 100, 100])
    upper_red = np.array([179, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask_blue = cv.inRange(hsv, lower_blue, upper_blue)
    mask_green = cv.inRange(hsv, lower_green, upper_green)
    mask_red = cv.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image
    result_blue = cv.bitwise_and(frame, frame, mask=mask_blue)
    result_green = cv.bitwise_and(frame, frame, mask=mask_green)
    result_red = cv.bitwise_and(frame, frame, mask=mask_red)

    cv.imshow('frame', frame)
    cv.imshow('mask_blue', mask_blue)
    cv.imshow('mask_green', mask_green)
    cv.imshow('mask_red', mask_red)
    cv.imshow('result_blue', result_blue)
    cv.imshow('result_green', result_green)
    cv.imshow('result_red', result_red)

    merged_ = cv.add(result_blue, result_green)
    merged = cv.add(merged_, result_red)
    cv.imshow("result", merged)

    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
cap.release()
