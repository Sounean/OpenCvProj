
# addWeighted(图1，图1的权重，图2，图2的权重，两张图都加(静态权重))
# 注意：仅图像宽高一样的情况下才能进行溶合 因为它本质是化成矩阵之后的运算，而矩阵加减的运算前提是矩阵宽高一致
import cv2 as cv
import numpy as np

back = cv.imread('face1.jpg')
smallcat = cv.imread('image01.jpg')

# print(back.shape)   #(1280, 2271, 3)
# print(smallcat.shape)   #(960, 960, 3) 此时两张图宽高还不一致，那就得拉伸

back_1 = cv.resize(back , (960,960))
print(back_1.shape) #(960, 960, 3)

result = cv.addWeighted(smallcat , 0.7 , back_1 , 0.3 , 0)
cv.imshow('result' ,result)
cv.waitKey(0)

