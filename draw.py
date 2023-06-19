import cv2 as cv
import numpy as np

blank = np.zeros((520,520,3), dtype='uint8')
# cv.imshow('Black', blank)

blank[:,:] = 255,255,255
# cv.imshow('White', blank)

cv.rectangle(blank, (10,10), (250,250), (0,0,0), thickness=2)
# cv.imshow('Rectangle', blank)

cv.rectangle(blank, (10,10), (250,250), (0,0,0), thickness=-1)
# cv.imshow('Rectangle_Filled', blank)

cv.rectangle(blank, (260,10), (500,250), (0,0,0), thickness=-1)
cv.rectangle(blank, (10,260), (250,500), (0,0,0), thickness=-1)
cv.rectangle(blank, (260,260), (500,500), (0,0,0), thickness=-1)
# cv.imshow('Window', blank)

blank[:,:] = 255,255,255
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,0), thickness=-1)
# cv.imshow('Circle', blank)

cv.line(blank, (0,0), (520,520), (0,0,0), thickness=2)
cv.line(blank, (520,0), (0,520), (0,0,0), thickness=2)
# cv.imshow('Line', blank)

blank[:,:] = 255,255,255
cv.putText(blank, ' Hello World', (10,50), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,0), thickness=2)
# cv.imshow('Text', blank)

cv.waitKey(0)