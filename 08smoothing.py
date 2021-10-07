#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# created by user12043 on 29.09.2021 - 10:24
# part of project opencv-tutorial

# https://docs.opencv.org/4.5.3/d4/d13/tutorial_py_filtering.html

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 2D CONVOLUTION
img = cv.imread("img/eagle.jpg")
cv.cvtColor(img, cv.COLOR_BGR2RGB, img)

# kernel = np.ones((5, 5), np.float32) / 25
kernel = np.ones((10, 10), np.float32) / 100
out = cv.filter2D(img, -1, kernel)

plt.subplot(121), plt.imshow(img), plt.title("input")
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(out), plt.title("output")
plt.xticks([]), plt.yticks([])

# IMAGE BLURRING
# Avaraging
plt.figure()
blur = cv.blur(img, (5, 5))
blur_box = cv.boxFilter(img, -1, (5, 5), normalize=False)
blur_box_n = cv.boxFilter(img, -1, (5, 5))

plt.subplot(221), plt.imshow(img), plt.title("input")
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(blur), plt.title("Blur")
plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(blur_box), plt.title("Blur Box")
plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(blur_box_n), plt.title("Blur Box Normalized")
plt.xticks([]), plt.yticks([])

# Gaussian Blur
plt.figure()
# cv.getGaussianKernel((5, 5), 1)
blur_g = cv.GaussianBlur(img, (5, 5), 0)
plt.subplot(221), plt.imshow(img), plt.title("input")
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(blur_g), plt.title("Gaussian Blur")
plt.xticks([]), plt.yticks([])

# Median Blur
blur_m = cv.medianBlur(img, 5)
plt.subplot(223), plt.imshow(blur_m), plt.title("Median Blur")
plt.xticks([]), plt.yticks([])

# Bilateral Filtering
blur_b = cv.bilateralFilter(img, 9, 75, 75)
plt.subplot(224), plt.imshow(blur_m), plt.title("Bilateral Filter")
plt.xticks([]), plt.yticks([])

plt.show()
