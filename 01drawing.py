#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# created by user12043 on 20.07.2021 - 19:07
# part of project opencv-tutorial

import numpy as np
import cv2 as cv

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)
# Draw a diagonal blue line with thickness of 5 px
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
cv.rectangle()
cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
