import cv2 as cv
img = cv.imread('datas/images/lena.png')
cv.imshow('lena',img)
cv.waitKey(0)