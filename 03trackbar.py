#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# created by user12043 on 22.07.2021 - 16:30
# part of project opencv-tutorial

import cv2 as cv
import numpy as np


def nothing(x):
    pass


image = np.zeros((640, 480, 3), np.uint8)
window_name = "image"
cv.namedWindow(window_name)

cv.createTrackbar("red", window_name, 0, 255, nothing)
cv.createTrackbar("green", window_name, 0, 255, nothing)
cv.createTrackbar("blue", window_name, 0, 255, nothing)

switch = '0: OFF\n1: ON'
cv.createTrackbar(switch, window_name, 0, 1, nothing)

while True:
    cv.imshow(window_name, image)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    r = cv.getTrackbarPos('red', window_name)
    g = cv.getTrackbarPos('green', window_name)
    b = cv.getTrackbarPos('blue', window_name)
    s = cv.getTrackbarPos(switch, window_name)

    if s == 0:
        image[:] = 0
    else:
        image[:] = b, g, r

cv.destroyAllWindows()
