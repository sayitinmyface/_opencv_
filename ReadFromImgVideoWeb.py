import cv2 as cv

def main():
    frame_h = 480
    frame_w = 640
    v_cap = cv.VideoCapture('datas/video/Armbot.mp4')
    w_cap = cv.VideoCapture(0)
    w_cap.set(4,frame_h)#enum  	cv::VideoCaptureProperties //CAP_PROP_FRAME_HEIGHT 
    w_cap.set(3,frame_w)#enum  	cv::VideoCaptureProperties //CAP_PROP_FRAME_WIDTH 
    ch_mode = ord('i')
    while 1:        
        if ch_mode==ord('i'):
            ch_mode = readImg()
        if ch_mode==ord('v'):
            ch_mode = readVideo(v_cap,frame_h,frame_w)
        if ch_mode==ord('w'):
            ch_mode = readWeb(w_cap)
        if ch_mode==ord('q'):
            break
        # ch_mode = cv.waitKey(1)
    v_cap.release()
    w_cap.release()
    cv.destroyAllWindows()

def readImg():
    img = cv.imread('datas/images/lena.png')
    cv.imshow('show',img)
    ch_mode = -1
    while 1:
        ch_mode = cv.waitKey(1)
        if ch_mode!=-1:
            break
    return ch_mode
def readVideo(v_cap,frameH,frameW):
    ch_mode = -1
    while 1:
        success,img = v_cap.read()
        img = cv.resize(img,(frameH,frameW))
        cv.imshow('show',img)
        ch_mode = cv.waitKey(1)
        if ch_mode!=-1:
            break
    return ch_mode
def readWeb(w_cap):
    ch_mode = -1
    while 1:
        success,img = w_cap.read()
        cv.imshow('show',img)
        ch_mode = cv.waitKey(1)
        if ch_mode!=-1:
            break
    return ch_mode
if __name__ == "__main__":
    print('1')
    main()

    

    