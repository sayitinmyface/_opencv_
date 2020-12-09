import cv2 as cv
import numpy as np

img = np.zeros((512,512,3),np.uint8)
print(img)
img[:] = 255,0,0
print(img.shape)

cv.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
cv.imshow('image',img)
cv.waitKey(0)
cv.rectangle(img,(0,0),(250,350),(0,0,255),2)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()