#图像轮廓指具有相同颜色(说明不用先二值化，彩色的也行)或强度的连续点的曲线

import cv2 as cv
import numpy as np
import argparse
import imutils

image = cv.imread('twoPic.png')


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", default='images/shapes.png',
	help="path to the input image")
args = vars(ap.parse_args())

# load the input image and convert it to grayscale

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# blur the image (to reduce false-positive detections) and then
# perform edge detection
blurred = cv.GaussianBlur(gray, (5, 5), 0)
edged = cv.Canny(blurred, 50, 130)  #显示轮框图
cv.imshow("blur",blurred)
cv.imshow('edged',edged)
#轮廓图中，寻找轮廓列表，初始化计算为0
# find contours in the edge map and initialize the total number of
# shapes found
cnts = cv.findContours(edged.copy(), cv.RETR_EXTERNAL,
	cv.CHAIN_APPROX_SIMPLE)
print(cnts)
cnts = imutils.grab_contours(cnts)
total = 0
#循环每一个轮廓，计算轮廓包含的面积像素个数，太小（25），就认为是噪声，忽略掉。正常的话，画图轮廓，计数+1。
# loop over the contours one by one
for c in cnts:
    # if the contour area is small, then the area is likely noise, so
    # we should ignore the contour
    if cv.contourArea(c) < 25:
        continue

    # otherwise, draw the contour on the image and increment the total
    # number of shapes found
    cv.drawContours(image, [c], -1, (204, 0, 255), 2)
    total += 1
#打印出总物体个数，并显示勾画轮廓的图形。
# show the output image and the final shape count
print("[INFO] found {} shapes".format(total))
cv.imshow("Image", image)
cv.waitKey(0)


cv.imshow('img' , image)










cv.waitKey(0)