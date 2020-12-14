import cv2 as cv
import numpy as np

def main():
    frameW = 640
    frameH = 480
    dir_name = 'datas/videos/roadway_01.mp4'
    cap = cv.VideoCapture(dir_name)
    # cap.set(4,frameH)#enum  	cv::VideoCaptureProperties //CAP_PROP_FRAME_HEIGHT 
    # cap.set(3,frameW)#enum  	cv::VideoCaptureProperties //CAP_PROP_FRAME_WIDTH 
    cv.namedWindow('canny')
    cv.createTrackbar('low','canny',0,1000,nothing)
    cv.createTrackbar('high','canny',0,1000,nothing)
    xx,yy = 40,475
    while 1:
        _,img_og = cap.read()
        if not _ :
            cap = cv.VideoCapture(dir_name)
            _,img_og = cap.read()
        #
        # img = cv.resize(img,(640,480))
        low = cv.getTrackbarPos('low','canny')
        high = cv.getTrackbarPos('high','canny')
        img = img_og[350:700,270:1000]#[1:2].. 1는 행위 범위 , 2는 열의 범위
        img = cv.resize(img,(frameW,frameH))
        # img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        # img = threholding(img,cv.THRESH_BINARY)
        # img = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,11,4)
        # img = cv.Canny(img,low,high)
        cv.line(img,(xx,yy),(xx-10,yy-10),(0,0,255),3)
        # cv.imshow('og',img)
        cv.imshow('canny',img)
        if cv.waitKey(5)==ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()
# 
def threholding(img,type_):
    return cv.threshold(img,50,255,type_)[1]    
    # 
def nothing():
    pass
if __name__ == "__main__":
    main()