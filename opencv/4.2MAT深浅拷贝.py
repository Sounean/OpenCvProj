#MAT实际上就是一个矩阵，可能有多个通道
#用了MAT好处：用了Mat可以直接用矩阵形式访问和操作图像
#每个Mat都由两大部分组成：Header（存放属性，维数、行列数、存储数据的指针、引用计数（防止内存泄漏））和Data(存放具体的数据）

import cv2 as cv
import numpy as np

img = cv.imread('image01.jpg')
img2 = img  #浅拷贝

img3 = img.copy()   #深拷贝
img[10:100 , 10:100] = [0,0,255]

cv.imshow('img' , img)
cv.imshow('img2' , img2)
cv.imshow('img3' , img3)


cv.waitKey(0)