import cv2 as cv
import numpy as np

img = cv.imread('image01.jpg')

#shape属性中包括了三个信息（高度，长度，通道数）
print(img.shape)

#图像占用多大空间
#长度*高度*通道数
print(img.size)

#图像中每个元素的位深
print(img.dtype)