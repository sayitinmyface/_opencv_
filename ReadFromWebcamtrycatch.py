import cv2 as cv
frame_h = 480
frame_w = 640
cap = cv.VideoCapture(0)
cap.set(4,frame_h)#enum  	cv::VideoCaptureProperties //CAP_PROP_FRAME_HEIGHT 
cap.set(3,frame_w)#enum  	cv::VideoCaptureProperties //CAP_PROP_FRAME_WIDTH 
if cap.isOpened():
    while 1:
        success,img = cap.read()
        if not success:
            break
        if cv.waitKey(1)==27:
            break
        cv.imshow('show',img)
cap.release()        
cv.destroyAllWindows()
