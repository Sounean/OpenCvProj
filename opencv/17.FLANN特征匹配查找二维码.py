import cv2 as cv
import numpy as np

# img1 = cv.imread('opencv_search.png')   #1.打开图片
img1 = cv.imread('scan01.jpg')
# img2 = cv.imread('opencv_orig.png')
img2 = cv.imread('scanfeature.png')

gray1 = cv.cvtColor(img1 , cv.COLOR_BGR2GRAY)
gray2 = cv.cvtColor(img2 , cv.COLOR_BGR2GRAY)

sitf = cv.SIFT_create() #2.1创建SIFT特征检测器对象

kp1 , des1 = sitf.detectAndCompute(gray1 , None)    #2.2通过sitf对象获得两个图的获取特征点和描述子
kp2 , des2 = sitf.detectAndCompute(gray2 , None)

#创建匹配器
index_params = dict(algorithm = 1 ,trees = 5)
search_params = dict(checks = 50)
flann = cv.FlannBasedMatcher(index_params , search_params)

matchs = flann.knnMatch(des1 , des2 , k=2)#对描述子进行匹配计算

good = []
for i,(m,n) in enumerate(matchs):
    if m.distance <0.7 * n.distance:    #小于一定差距表示是一个不错的匹配点(越小表明要求越高，那么得到的点也就越少)
        good.append(m)

ret = cv.drawMatchesKnn(img1 , kp1 , img2 , kp2 ,[good] ,None)

cv.imshow('result' , ret)
cv.waitKey(0)