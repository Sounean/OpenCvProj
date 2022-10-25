#是Harris检测的微调   (Harris需要根据经验对k进行调整，Shi-Tomasi可以不用对k专门考虑应该设什么最佳)

import cv2 as cv
import numpy as np

maxCorners = 1000
ql = 0.01
minDistance = 10    #
blockSize = 2
ksize = 3
k = 0.04
img = cv.imread('chess.png')
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

# （源图 ， 角点最大数(值0表示全返回) , 质量（0.0.1~0.1之间） , 角之间距离 ， mask：感兴趣的区域 , 检测窗口 ， 是否使用Harris算法 , 默认0.04）
corners = cv.goodFeaturesToTrack(gray , maxCorners , ql , minDistance)  #返回坐标
corners = np.int0(corners)

for i in corners:   #Shi-Tomasi绘制角点
    x,y = i.ravel() #获取一维数组
    cv.circle(img , (x,y) , 3 , (255,255,0) , -1)



cv.imshow('harris' , img)
cv.waitKey(0)
