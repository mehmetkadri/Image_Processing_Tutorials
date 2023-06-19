import cv2 as cv

img = cv.imread('diagnosis_images/nevus/ISIC_0031434.jpg')

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()

def hair_remove(img):
    # convert image to grayScale
    grayScale = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

    # kernel for morphologyEx
    kernel = cv.getStructuringElement(1,(17,17))

    # apply MORPH_BLACKHAT to grayScale image
    blackhat = cv.morphologyEx(grayScale, cv.MORPH_BLACKHAT, kernel)

    # apply thresholding to blackhat
    _,threshold = cv.threshold(blackhat,10,255,cv.THRESH_BINARY)

    # inpaint with original image and threshold image
    final_image = cv.inpaint(img,threshold,1,cv.INPAINT_TELEA)

    return final_image

final_image = hair_remove(img)

cv.imshow('final_image', final_image)
cv.waitKey(0)
cv.destroyAllWindows()