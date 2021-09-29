#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# created by user12043 on 14.09.2021 - 16:10
# part of project opencv-tutorial

# https://docs.opencv.org/4.5.3/d7/d4d/tutorial_py_thresholding.html

import cv2 as cv
import matplotlib.pyplot as plt

# SIMPLE THRESHOLDING

# Input should be gray-scale image
# img_color = cv.imread("img/black_white_gradiant.png")
# img = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
img = cv.imread("img/black_white_gradiant.png", 0)
img = cv.resize(img, None, fx=0.5, fy=0.5)

ret, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
ret, thresh3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
ret, thresh4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
ret, thresh5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

titles = ["Original Image", "BINARY", "BINARY_INV", "TRUNC", "TOZERO", "TOZERO_INV"]
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], "gray", vmin=0, vmax=255)
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
# plt.show()

# ADAPTIVE THRESHOLDING

img = cv.imread("img/sudoku.jpg", 0)
# Notice the median blur before
img = cv.medianBlur(img, 5)
mean_threshold = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
gauss_threshold = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

plt.figure()
plt.subplot(1, 2, 1), plt.imshow(mean_threshold, "gray")
plt.title("MEAN_THRESHOLD")
plt.subplot(1, 2, 2), plt.imshow(gauss_threshold, "gray")
plt.title("GAUSSIAN_THRESHOLD")

# plt.show()

# OTSU
plt.figure()
img = cv.imread("img/noisy2.png", 0)
ret1, thresh1 = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
plt.subplot(2, 2, 1), plt.imshow(thresh1, "gray")
plt.title("OTSU")
plt.subplot(2, 2, 2), plt.hist(thresh1.ravel(), 256)

blur = cv.GaussianBlur(img, (5, 5), 0)
ret2, thresh2 = cv.threshold(blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
plt.subplot(2, 2, 3), plt.imshow(thresh2, "gray")
plt.title("OTSU with Blur")
plt.subplot(2, 2, 4), plt.hist(thresh2.ravel(), 256)
plt.show()
