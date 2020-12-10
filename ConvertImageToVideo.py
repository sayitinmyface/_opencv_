import cv2 as cv
import os

def main():
    dname = os.getcwd()+'/datas/images/imageframes'
    files = os.listdir(dname)
    fname = dname+'/image_0.png'
    img = cv.imread(fname)
    h,w,l = img.shape
    size = (w,h)
    fps = 0.5
    fname_output = dname+'/output_video.avi'
    out_avi = cv.VideoWriter(fname_output,cv.VideoWriter_fourcc(*'DIVX'),fps,size)
    for count in range(len(files)):
        fname = dname+'/image_'+str(count)+'.png'
        img = cv.imread(fname)
        if img is not None:
            cv.imshow('image_',img)
            out_avi.write(img)
            cv.waitKey(1)

def play():
    cap = cv.VideoCapture('data/image/imageframes/output_video.avi')
    while 1:
        _,img = cap.read()
        cv.imshow('avi',img)            
        cv.waitKey(1)
if __name__ == "__main__":
    main()
    # play()