#图像轮廓指具有相同颜色(说明不用先二值化，彩色的也行)或强度的连续点的曲线

import cv2 as cv
import numpy as np
import argparse
import imutils
min_w = 100
min_h = 100
modelNum = 0    #金属物体的个数

kernel = cv.getStructuringElement(cv.MORPH_RECT , (5,5))    # 5*5 小矩阵
#image = cv.imread('onePic.png')
# image1 = cv.imread('110901.jpg')
image = cv.imread('scan01.jpg')

# image = cv.resize(image1 , dsize=(1000,500))


gray_img = cv.cvtColor(image , cv.COLOR_BGR2GRAY)
gaussian_dst = cv.GaussianBlur(gray_img , (7 , 7) , sigmaX=1)  #去噪
cv.imshow('gaussian_dst' , gaussian_dst)

ret , dst = cv.threshold(gaussian_dst , 165 , 255 , cv.THRESH_BINARY)   # 设阈值
cv.imshow('bin' , dst)

erode = cv.erode(dst , kernel , iterations=2) #腐蚀
cv.imshow('erode' , erode)

# dst = cv.morphologyEx(dilate  , cv.MORPH_OPEN , kernel)    #开运算去除小块
# cv.imshow('dst' , dst)

#
# close = cv.morphologyEx(erode , cv.MORPH_CLOSE , kernel) #闭运算 (无太大用)
# cv.imshow('close'  , close)

ret , dst = cv.threshold(gaussian_dst , 0 , 255 , cv.THRESH_BINARY)   # 设阈值
cnts , h = cv.findContours(dst , cv.RETR_TREE , cv.CHAIN_APPROX_SIMPLE)
for (i, c) in enumerate(cnts):
    (x, y, w, h) = cv.boundingRect(c)  # 获得x，y，宽和高
    isValid = (w >= min_w) and (h >= min_h)
    if (not isValid):
        continue
    cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    modelNum+=1

image1 = cv.resize(image , dsize=(1000,500))
cv.imshow('out1' , image1)
print("out1的金属物体数量为:%d"%(modelNum))








# # 图2
# modelNum = 0
# image2 = cv.resize(cv.imread('110902.jpg') , dsize=(1000,500))
# gaussian_dst2 = cv.GaussianBlur(cv.cvtColor(image2 , cv.COLOR_BGR2GRAY) , (7 , 7) , sigmaX=1)  #去噪
# ret , dst = cv.threshold(gaussian_dst , 150 , 255 , cv.THRESH_BINARY)   # 设阈值
# dilate = cv.dilate(dst , kernel , iterations=3) #膨胀 (小螺丝钉)
# cnts , h = cv.findContours(close , cv.RETR_TREE , cv.CHAIN_APPROX_SIMPLE)
# for (i, c) in enumerate(cnts):
#     (x, y, w, h) = cv.boundingRect(c)  # 获得x，y，宽和高
#     isValid = (w >= min_w) and (h >= min_h)
#     if (not isValid):
#         continue
#     cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
#     modelNum+=1
# cv.imshow('out2' , image2)
# print("out1的金属物体数量为:%d"%(modelNum))
#
# #图3
# modelNum = 0
# image3 = cv.resize(cv.imread('110903.jpg') , dsize=(1000,500))
# gaussian_dst2 = cv.GaussianBlur(cv.cvtColor(image3 , cv.COLOR_BGR2GRAY) , (7 , 7) , sigmaX=1)  #去噪
# ret , dst = cv.threshold(gaussian_dst , 150 , 255 , cv.THRESH_BINARY)   # 设阈值
# dilate = cv.dilate(dst , kernel , iterations=3) #膨胀 (小螺丝钉)
# cnts , h = cv.findContours(close , cv.RETR_TREE , cv.CHAIN_APPROX_SIMPLE)
# for (i, c) in enumerate(cnts):
#     (x, y, w, h) = cv.boundingRect(c)  # 获得x，y，宽和高
#     isValid = (w >= min_w) and (h >= min_h)
#     if (not isValid):
#         continue
#     cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
#     modelNum+=1
# cv.imshow('out3' , image3)
# print("out1的金属物体数量为:%d"%(modelNum))
#
# #图4
# modelNum = 0
# image3 = cv.resize(cv.imread('110904.jpg') , dsize=(1000,500))
# gaussian_dst2 = cv.GaussianBlur(cv.cvtColor(image3 , cv.COLOR_BGR2GRAY) , (7 , 7) , sigmaX=1)  #去噪
# ret , dst = cv.threshold(gaussian_dst , 150 , 255 , cv.THRESH_BINARY)   # 设阈值
# dilate = cv.dilate(dst , kernel , iterations=3) #膨胀 (小螺丝钉)
# cnts , h = cv.findContours(close , cv.RETR_TREE , cv.CHAIN_APPROX_SIMPLE)
# for (i, c) in enumerate(cnts):
#     (x, y, w, h) = cv.boundingRect(c)  # 获得x，y，宽和高
#     isValid = (w >= min_w) and (h >= min_h)
#     if (not isValid):
#         continue
#     cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
#     modelNum+=1
# cv.imshow('out4' , image3)
# print("out1的金属物体数量为:%d"%(modelNum))



# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", default='images/shapes.png',
# 	help="path to the input image")
# args = vars(ap.parse_args())
#
# # load the input image and convert it to grayscale
#
# gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)
#
# # blur the image (to reduce false-positive detections) and then
# # perform edge detection
# blurred = cv.GaussianBlur(gray, (5, 5), 0)
# edged = cv.Canny(blurred, 50, 130)  #显示轮框图
# cv.imshow("blur",blurred)
# cv.imshow('edged',edged)
# #轮廓图中，寻找轮廓列表，初始化计算为0
# # find contours in the edge map and initialize the total number of
# # shapes found
# cnts = cv.findContours(edged.copy(), cv.RETR_EXTERNAL,
# 	cv.CHAIN_APPROX_SIMPLE)
# print(cnts)
# cnts = imutils.grab_contours(cnts)
# total = 0
# #循环每一个轮廓，计算轮廓包含的面积像素个数，太小（25），就认为是噪声，忽略掉。正常的话，画图轮廓，计数+1。
# # loop over the contours one by one
# for c in cnts:
#     # if the contour area is small, then the area is likely noise, so
#     # we should ignore the contour
#     if cv.contourArea(c) < 25:
#         continue
#
#     # otherwise, draw the contour on the image and increment the total
#     # number of shapes found
#     cv.drawContours(image, [c], -1, (204, 0, 255), 2)
#     total += 1
# #打印出总物体个数，并显示勾画轮廓的图形。
# # show the output image and the final shape count
# print("[INFO] found {} shapes".format(total))
# cv.imshow("Image", image)
# cv.waitKey(0)

# cv.imshow('image' , image)
# cv.imshow('gray' , gray_img)










cv.waitKey(0)