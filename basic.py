import cv2 as cv

# Original image
img = cv.imread('./Photos/cat1.jpg')
#cv.imshow('cat', img)

# Converting image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('gray', gray)

# Blurring image
blur = cv.GaussianBlur(img, (17,17), 0)
#cv.imshow('blur', blur)

# Edge cascade
canny = cv.Canny(img, 100, 200)
#cv.imshow('canny', canny)

# Dilating the image
dilated = cv.dilate(canny, (3,3), iterations=1)
#cv.imshow('dilated', dilated)

# Eroding the image
eroded = cv.erode(dilated, (3,3), iterations=1)
#cv.imshow('eroded', eroded)

# Resize the image
resized = cv.resize(img, (img.shape[1]//2, img.shape[0]//2), interpolation =cv.INTER_CUBIC)
#cv.imshow('resized', resized)

# Cropping the image
cropped = img[0:img.shape[0]//2, 0:img.shape[1]//2]
#cv.imshow('cropped', cropped)

cv.waitKey(0)