import cv2 as cv
import numpy as np

img = cv.imread('image01.jpg')

logo = np.zeros((200,200,3) , np.uint8)

mask = np.zeros((200,200) , np.uint8)

logo[20:120 , 20:120] = [0,0,255]
logo[80:180 , 80:180] = [0,255,0]

cv.imshow('logo' , logo)
# cv.waitKey(0)

mask[20:120 , 20:120] = 255
mask[80:180 , 80:180] = 255
cv.imshow('mask' , mask)
# cv.waitKey(0)

m = cv.bitwise_not(mask)    #对掩码按位取反

roi = img[0:200 , 0:200]    #选择img添加logo的位子

tmp = cv.bitwise_and(roi , roi ,mask = m)
