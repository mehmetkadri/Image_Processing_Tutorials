import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('./Photos/dog2.jpg')
cv.imshow('Original', img)

# Plotting the image
plt.imshow(img)
#plt.show()

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
#cv.imshow('HSV', hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
#cv.imshow('L*a*b', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
#cv.imshow('RGB', rgb)

# HSV to BGR
bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
#cv.imshow('HSV to BGR', bgr)

# Plotting the image as RGB
plt.imshow(rgb)
#plt.show()

cv.waitKey(0)