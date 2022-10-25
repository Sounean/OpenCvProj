# 使用第一组中的每个特征的描述子与第二组中所有特征描述子进行匹配,计算它们的差距，返回一个最接近的匹配
#特征匹配步骤：1.创建匹配器 2.进行特征匹配 3.绘制匹配点
import cv2 as cv
import numpy as np

img1 = cv.imread('opencv_search.png')   #1.打开图片
img2 = cv.imread('opencv_orig.png')

gray1 = cv.cvtColor(img1 , cv.COLOR_BGR2GRAY)
gray2 = cv.cvtColor(img2 , cv.COLOR_BGR2GRAY)

sitf = cv.SIFT_create() #2.1创建SIFT对象

kp1 , des1 = sitf.detectAndCompute(gray1 , None)    #2.2通过sitf对象获得两个图的获取特征点和描述子
kp2 , des2 = sitf.detectAndCompute(gray2 , None)

bf = cv.BFMatcher(cv.NORM_L1)   #3.1创建BFMatcher对象
match = bf.match(des1,des2)

img3 = cv.drawMatches(img1 , kp1 , img2 , kp2 , match , None)#3.2通过BFMatcher来获得两张图象的匹配的结果

cv.imshow('img3' , img3)
cv.waitKey(0)

