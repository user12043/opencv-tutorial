#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# created by user12043 on 22.07.2021 - 17:32
# part of project opencv-tutorial

import cv2 as cv


def show_and_wait(img):
    cv.imshow('res', img)
    cv.waitKey(0)


# Load two images
img1 = cv.imread('img/eagle.jpg')
img2 = cv.imread('img/logo.png')
# I want to put logo on top-left corner, So I create a ROI
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]
# Now create a mask of logo and create its inverse mask also
img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 20, 255, cv.THRESH_BINARY)
# show_and_wait(mask)
mask_inv = cv.bitwise_not(mask)
# Now black-out the area of logo in ROI
img1_bg = cv.bitwise_and(roi, roi, mask=mask_inv)
show_and_wait(img1_bg)
# Take only region of logo from logo image.
img2_fg = cv.bitwise_and(img2, img2, mask=mask)
show_and_wait(img2_fg)
# Put logo in ROI and modify the main image
dst = cv.add(img1_bg, img2_fg)
show_and_wait(img2_fg)
img1[0:rows, 0:cols] = dst
cv.imshow('res', img1)
cv.waitKey(0)
cv.destroyAllWindows()
