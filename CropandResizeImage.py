import cv2 as cv
import os

def main():
    img = cv.imread('datas/images/lambo.png')
    cv.imshow('image',img)

    # imgR = cv.resize(img,(1000,500))
    # cv.imshow('imageR',imgR)

    imgC = img[46:219,152:495]
    cv.imshow('imageC',imgC)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()