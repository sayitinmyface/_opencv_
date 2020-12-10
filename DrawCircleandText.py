import cv2 as cv


img = cv.imread('datas/images/load_image.jpg')

cir_x ,cir_y = 60,img.shape[0]-30
rec_x , rec_y = 50,60
radius = 15
# 
cv.rectangle(img,(rec_x,rec_y),(rec_x+70,rec_y+70),(0,0,255),3)
cv.circle(img,(cir_x,cir_y),radius,(0,234,0),2,cv.FILLED)
cv.circle(img,(rec_x+185,rec_y+35),45,(0,0,255),2,0)
cv.rectangle(img,(rec_x+350,rec_y+170),(rec_x+420,rec_y+240),(0,0,255),3)
cv.rectangle(img,(rec_x+280,rec_y+220),(rec_x+350,rec_y+280),(0,0,255),3)



cv.imshow('show',img)
cv.waitKey(0)
cv.destroyAllWindows()