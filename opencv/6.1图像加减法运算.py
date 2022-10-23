import cv2 as cv
import numpy as np

#图的加法运算就是矩阵的加法运算    (所以两张图的长宽要一致) add(图1，矩阵1)
imgFace1 = cv.imread('face1.jpg')
cv.imshow('orig' , imgFace1)
# print(imgFace1.shape) #查看图片的（长，宽，通道数）
img = np.ones((1280, 2271, 3) , np.uint8) * 100
resultImg = cv.add(imgFace1 , img)
# cv.imshow('result' , resultImg)   #像曝光了一样
# cv.waitKey(0)

#图像的减法运算 cv.subtract(图A , B) A-B
orig_1 = cv.subtract(resultImg , img)
# cv.imshow('orig_1' , orig_1)
# cv.waitKey(0)

#图像乘除  cv.multiply(A,B)  cv.divide(A,B)