import cv2 as cv
frame_h = 480
frame_w = 640
cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH,frame_w)
cap.set(4,frame_h)
while True:
    success,img = cap.read()
    if not success:
        break
    cv.imshow('stream',img)  
    cv.waitKey(1)
cap.release()
