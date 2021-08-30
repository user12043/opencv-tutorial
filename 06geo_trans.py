#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# created by user12043 on 15.08.2021 - 12:55
# part of project opencv-tutorial

# https://docs.opencv.org/4.5.3/da/d6e/tutorial_py_geometric_transformations.html
import math
import numpy as np
import cv2 as cv

# Scaling
img = cv.imread("img/eagle_small.jpg")
cv.imshow("resize", cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC))
cv.waitKey(0)

height, width = img.shape[:2]
cv.imshow("resize2", cv.resize(img, (width // 2, height // 2), interpolation=cv.INTER_CUBIC))
cv.waitKey(0)

# Translation
# img_gr = cv.imread("img/eagle_small.jpg", 0)
# height, width = img_gr.shape
M = np.float32([[1, 0, 300], [0, 1, 300]])
# cv.imshow("translation", cv.warpAffine(img_gr, M, (width, height)))
cv.imshow("translation", cv.warpAffine(img, M, (width, height)))
cv.waitKey(0)

# Rotation
center = (width - 1) / 2.0, (height - 1) / 2.0
# 1. Manually make transformation matrix
# rotate angle = P => M = [[cosP, -sinP], [sinP, cosP]]
angle = np.deg2rad(90)
scale = 1.0  # 1 = do not change scale
alpha = scale * math.cos(angle)
beta = scale * math.sin(angle)
Mm = np.array([
    [alpha, beta, ((1.0 - alpha) * center[0]) - (beta * center[1])],
    [-beta, alpha, (beta * center[0]) + ((1.0 - alpha) * center[1])]
])
cv.imshow("rotate", cv.warpAffine(img, Mm, (width, height)))
cv.waitKey(0)

# 2. Easy way in documentation
angle = 90
M = cv.getRotationMatrix2D(center, angle, scale)
cv.imshow("rotate2", cv.warpAffine(img, M, (width, height)))
cv.waitKey(0)

# 3. Affline Transformation
rows, cols, ch = img.shape

# Determine points
pts_in_input = [[100, 100], [300, 100], [100, 250]]
pts_in_output = [[100, 200], [300, 100], [150, 300]]

# Mark points in input
for point in pts_in_input:
    img = cv.circle(img, point, 0, (0, 0, 255), 4)

M = cv.getAffineTransform(np.float32(pts_in_input), np.float32(pts_in_output))
dst = cv.warpAffine(img, M, (cols, rows))
cv.imshow("affline", dst)

cv.waitKey(0)
cv.destroyAllWindows()

# continue...
