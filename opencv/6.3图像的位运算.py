
import cv2 as cv
import numpy as np


img = np.zeros((200,200) , np.uint8)    # 创建一张黑白色的图片
img[20:120 , 20:120] = 255  #部分变成白色
cv.imshow('原图img' , img)
# cv.waitKey(0)

#非操作cv.bitwise_not(图片)   黑变白，白变黑
bitwiseNotImg = cv.bitwise_not(img)
# cv.imshow('非操作后' , bitwiseNotImg)
# cv.waitKey(0)

#与运算cv.imshow('img2' , img2)    两张图中同时位1即为1(白色)，其他均为0
img2 = np.zeros((200,200) , np.uint8)
img2[80:180 , 80:180] = 255
cv.imshow('img2' , img2)
bitwiseAndImg = cv.bitwise_and(img,img2)
cv.imshow('bitwiseAndImg'  ,bitwiseAndImg)
# cv.waitKey(0)

#或与异或运算   与是取交集  或只要是非0的都显示出来,无论是否是交集 异或：交集部分为0，非交集部分为1


