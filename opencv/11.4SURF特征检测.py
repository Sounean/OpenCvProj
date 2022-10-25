#SURF步骤：1.创建SURF对象，2.获取关键点和描述子 3.绘制关键点:drawKeypoints(gray,kp,img)
# 关键点：位置、大小和方向
import cv2 as cv
import numpy as np

img = cv.imread('chess.png')
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)




cv.imshow('SIFT' , img)
cv.waitKey(0)