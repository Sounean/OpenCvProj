import cv2 as cv
import numpy as np

blockSize = 2
ksize = 3
k = 0.04
img = cv.imread('chess.png')

#获取角点需要灰度化
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

#Harris角点检测
dst = cv.cornerHarris(gray , blockSize , ksize , k)

#img中的点，仅将大于dst最大值百分之一的显示出来
img[dst > 0.01*dst.max()] = [0,0,255]
cv.imshow('img' ,img)






cv.waitKey(0)