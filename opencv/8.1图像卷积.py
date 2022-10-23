import cv2 as cv
import numpy as np

img = cv.imread('test01.jpg')

kernel = np.ones((5,5) , np.float32) / 25   #一个每个元素均是1/25的5*5的矩阵
dst = cv.filter2D(img , -1 , kernel)    #卷积后的输出图像

cv.imshow('img' , img)
cv.imshow('dst' , dst)
cv.waitKey(0)