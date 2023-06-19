import cv2 as cv

# This works for photos, videos and live videos
def rescale_frame(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dim = (width, height)
    return cv.resize(frame, dim, interpolation =cv.INTER_AREA)

# This works for only live videos
def changeResolution(width, height, frame):
    
    capture.set(3, width)
    capture.set(4, height)


# Read image
img = cv.imread('./Photos/cat1.jpg')
resized_img = rescale_frame(img, scale=0.5)
cv.imshow('cat', resized_img)
cv.waitKey(0)

# Read video
capture = cv.VideoCapture('./Videos/cat.mp4')

while True:
    isTrue, frame= capture.read()

    frame_resized = rescale_frame(frame, scale=0.1)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('q'):
        break

capture.release()
cv.destroyAllWindows()
