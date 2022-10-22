import cv2 as cv
import numpy as np

img = np.zeros((480,640,3),np.uint8)

b,g,r = cv.split(img)   #分割3个通道

b[10:100 , 10:100] = 255
g[10:100 , 10:100] = 255

img2 = cv.merge(b,g,r)      #合并两个图层

cv.imshow('img',img)
cv.imshow('b' , b)  # 虽然是蓝色通道，但是仅1个通道，所以应该是白色
cv.imshow('g' , g)  #白色
cv.imshow('img2' , img2)    #合并(绿色加蓝色，左上角应该变成青色）

cv.waitKey(0)
