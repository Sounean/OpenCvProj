#1.创建Haar级联器  2.导入图片灰度化
#  源img , 缩放因子(因为可能不能刚好把人脸放进去)double scaleFactor = 1.1 , 人脸最小的像素值int)

import cv2 as cv
import numpy as np

#1.创建Haar级联器
facer = cv.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
eyer = cv.CascadeClassifier('./haarcascades/haarcascade_eye.xml')
#2.导入人脸识别的图片并将其灰度化
img = cv.imread('p3.png')
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

# #3. 进行人脸、眼识别
# faces = facer.detectMultiScale(gray , 1.1 , 5)  #返回值是[[x , y , w , h]]
# eyes = eyer.detectMultiScale(gray , 1.1 , 5)  #返回值是[[x , y , w , h]]
#
#
# for (x,y,w,h) in eyes:
#     cv.rectangle(img , (x,y) , (x+w,y+h) , (0,0,255) , 2)

#分别识别准确率不高，最好是在检测出人脸的基础上再进行检测眼睛
faces = facer.detectMultiScale(gray , 1.1 , 3)

i=0
for (x,y,w,h) in faces:
    cv.rectangle(img , (x,y) , (x+w,y+h) , (0,0,255) , 2)
    roi_img = img[y:y+h , x:x+w]    #扣出[x,y]到[x+w,y+h]的小方块
    eyes = eyer.detectMultiScale(roi_img , 1.1 , 5)  #返回值是[[x , y , w , h]]
    for (x,y,w,h) in eyes:
        cv.rectangle(roi_img , (x,y) , (x+w,y+h) , (0,0,255) , 2)
        i=i+1
        winname = "face" + str(i)
        cv.imshow(winname , roi_img)

cv.imshow('img',roi_img)
cv.waitKey(0)