import cv2 as cv
import numpy as np

img = cv.imread('image01.jpg')
#翻转cv.flip(img , 方向)
new = cv.flip(img , 0)  #0上下翻转，>0左右翻转,<0 上下+左右
cv.imshow('new' , new)
# cv.waitKey(0)

#旋转cv.rotate(img , 旋转的角度)   #顺时针旋转
rotateImg = cv.rotate(img , cv.ROTATE_90_CLOCKWISE)
cv.imshow('rotateImg' , rotateImg)
cv.waitKey(0)

