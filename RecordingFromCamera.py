import cv2 as cv
import os

def main():
    frame_h = 480
    frame_w = 640
    cap = cv.VideoCapture(0)
    cap.set(4,frame_h)
    cap.set(3,frame_w)
    cap.set(cv.CAP_PROP_FPS,20.0)
    size = (frame_w,frame_h)

    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out_avi = cv.VideoWriter('data/videos/output.avi',fourcc,20.0,size)
    fourcc = cv.VideoWriter_fourcc(*'MP4V')
    out_mp4 = cv.VideoWriter('datas/videos/output.mp4',fourcc,20.0,size)
    while 1:
        ret,frame = cap.read()
        out_avi.write(frame)
        out_mp4.write(frame)
        cv.imshow('show',frame)
        if cv.waitKey(1)==ord('q'):
            break
    cap.release()
    out_mp4.release()
    out_avi.release()

if __name__ == "__main__":
    main()