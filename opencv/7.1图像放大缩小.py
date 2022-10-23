import cv2 as cv
import numpy as np

#图像缩放resize( , ,  , x轴的缩放因子,y轴的缩放因子,插值算法)
#缩放算法：1.邻近插值：速度快，效果差
#        (默认的,速度快，效果好)2.双线性插值：原图中的4个点
#（效果好，时长更长）3.三次插值，原图中的16个点
img = cv.imread('image01.jpg')
img_1 = cv.resize(img , (400,400))

print(img.shape)

cv.imshow('img' , img)
cv.imshow('img_1' , img_1)
# cv.waitKey(0)

img_2 = cv.resize(img , None , fx=0.3 , fy=0.3)
cv.imshow('img_2' , img_2)
cv.waitKey(0)