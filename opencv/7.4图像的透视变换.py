#因为我们拍照肯定是歪歪扭扭的，可以通过透视变换把歪歪扭扭的变成正的

import cv2 as cv
import numpy as np

img = cv.imread('test01.jpg')
h,w,ch = img.shape
print(img.shape)

# 比仿射不同的是，仿射仅需要三个，但是透视变换需要四个坐标点 (即需要拉伸变换的四个角)
src = np.float32([[100,1100] , [1000,1100] , [0,1500] , [1100,1700]])  #原先的三个点 (竖着和横着来确定两条直线)
dst = np.float32([[0,0] , [1200,0] , [0,1600] , [1200,1700]])  #现在的三个点
M = cv.getPerspectiveTransform(src , dst)
new = cv.warpPerspective(img , M , (2300,3000))

cv.imshow('img' , img)
cv.imshow('new' , new)
cv.waitKey(0)