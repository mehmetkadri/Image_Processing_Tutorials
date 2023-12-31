import cv2 as cv
import numpy as np

img = cv.imread('./Photos/dog2.jpg')
cv.imshow('Original', img)

blank = np.zeros(img.shape, dtype='uint8')
#cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
#cv.imshow('Gray to Canny', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
#cv.imshow('Gray to Thresh', thresh)

contours, hierarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
#print(f'Number of contours in bw: {len(contours)}')

cv.drawContours(blank, contours, -1, (120, 170, 170), 1)
cv.imshow('Contours', blank)


cv.waitKey(0)