import cv2 as cv
frameW = 640
frameH = 480
cap = cv.VideoCapture('datas/videos/Armbot.mp4')
while True:
    success,img = cap.read()
    img = cv.resize(img,(frameW,frameH))
    cv.imshow('result',img)    
    if cv.waitKey(1)==ord('q'):
        break
cap.release()
