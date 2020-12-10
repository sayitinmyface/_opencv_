import cv2 as cv
import os
def main():
    filename = os.getcwd()+'/datas/videos/Armbot.mp4'
    cap = cv.VideoCapture(filename)
    sec = 0
    count = 0
    frameRate = 0.5
    success = cap.isOpened()
    while success:
        sec = sec + frameRate
        success = writeFrame(cap,sec,count)
        count = count+1

def writeFrame(vc,sec,count):
    dname = os.getcwd()+'/datas/images/imageframes'
    if not os.path.exists(dname):
        os.makedirs(dname)        
    vc.set(cv.CAP_PROP_POS_MSEC,sec*1000)
    hasF , img = vc.read()
    if hasF:
        cv.imwrite(dname+'/image_'+str(count)+'.png',img)
    # 
    return hasF

if __name__ == "__main__":
    main()

