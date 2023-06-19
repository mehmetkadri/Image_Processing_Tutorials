import cv2 as cv
import numpy as np

image = cv.imread('./Photos/dog2.jpg')
cv.imshow('dog', image)


# Translate image
def translate(image, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    return cv.warpAffine(image, transMat, (image.shape[1], image.shape[0]))
#cv.imshow('translated', translate(image, 10, 10))


# Rotate image
def rotate(image, angle, rotPoint=None):
    (h, w) = image.shape[:2]
    if rotPoint is None:
        rotPoint = (w / 2, h / 2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    return cv.warpAffine(image, rotMat, (w, h))
#cv.imshow('rotated', rotate(image, 45))


# Resizing image
#cv.imshow('resized', cv.resize(image, (400, 200), interpolation=cv.INTER_AREA))


# Flipping image
#cv.imshow('flipped', cv.flip(image, 1))


# Cropping image
cv.imshow('cropped', image[30:280, 500:800])

cv.waitKey(0)