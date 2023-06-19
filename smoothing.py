import cv2 as cv
import numpy as np

img = cv.imread('./Photos/dog2.jpg')
cv.imshow('Original', img)

# Average
average = cv.blur(img, (5, 5))
cv.imshow('Average', average)

# Gaussian
gaussian = cv.GaussianBlur(img, (5, 5), 0)
cv.imshow('Gaussian', gaussian)

# Median
median = cv.medianBlur(img, 5)
cv.imshow('Median', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 9, 75, 75)
cv.imshow('Bilateral', bilateral)


#save image as png
cv.imwrite('dog2_bilateral.png', bilateral)

cv.waitKey(0)