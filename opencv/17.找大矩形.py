import cv2 as cv
import numpy as np

min_w = 200
min_h = 200
kernel = cv.getStructuringElement(cv.MORPH_RECT , (5,5))    # 5*5 小矩阵

image = cv.imread('scan01.jpg')

# image = cv.resize(image1 , dsize=(1000,500))


gray_img = cv.cvtColor(image , cv.COLOR_BGR2GRAY)
gaussian_dst = cv.GaussianBlur(gray_img , (7 , 7) , sigmaX=1)  #去噪
cv.imshow('gaussian_dst' , gaussian_dst)

ret , dst = cv.threshold(gaussian_dst , 165 , 255 , cv.THRESH_BINARY)   # 设阈值
cv.imshow('bin' , dst)

erode = cv.erode(dst , kernel , iterations=2) #腐蚀
cv.namedWindow('erode1',0)
cv.imshow('erode1' , erode)
cnts , h = cv.findContours(erode , cv.RETR_TREE , cv.CHAIN_APPROX_SIMPLE) # 获取所有矩形
for (i, c) in enumerate(cnts):
    (x, y, w, h) = cv.boundingRect(c)  # 获得x，y，宽和高
    isValid = (w >= min_w) and (h >= min_h)
    if (not isValid):
        continue
    cv.rectangle(erode, (x, y), (x + w, y + h), (255, 255, 255), -1)

cv.namedWindow('erode2',0)
cv.imshow('erode2' , erode) #成功获取三个大的矩形

cnts , h = cv.findContours(erode , cv.RETR_TREE , cv.CHAIN_APPROX_SIMPLE) # 获取三个大圆形
for (i, c) in enumerate(cnts):
    (x, y, w, h) = cv.boundingRect(c)  # 获得x，y，宽和高
    cv.rectangle(image, (x, y), (x + w, y + h), (100, 100, 100), 2)

cv.namedWindow('final',0)
cv.imshow('final' , image) #成功获取三个大的矩形

cv.waitKey(0)
cv.destroyAllWindows()