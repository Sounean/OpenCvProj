#仿射变换是图像旋转、缩放、平移的总称

import cv2 as cv
import numpy as np

# 平移：cv.warpAffine(img， M变换矩阵 , 输出尺寸大小 , 插值算法 , 边界外推法标志 ， 填充边界的值）
# 平移矩阵： 矩阵中的每个像素由（x,y）组成，则变换矩阵为2*2的矩阵。若平移量为2*1的向量，则平移矩阵为2*3矩阵
img = cv.imread('image01.jpg')
h,w,ch = img.shape
M = np.float32([[1,0,100] , [0,1,0]])   #x方向上偏移100，y方向上不变
new = cv.warpAffine(img , M , (w,h))

cv.imshow('img' , img)
cv.imshow('new' , new)
# cv.waitKey(0)

#计算变换的M函数：cv.getRotationMatrix2D(中心点，角度，缩放比例)   #旋转的角度为逆时针
M = cv.getRotationMatrix2D((100,100) , 15 , 1.0)    #这里给出来api给我，我们对应的放进去可以帮我们计算出来M
img_1 = cv.warpAffine(img , M , (w,h))

cv.imshow("img_1" , img_1)
# cv.waitKey(0)

#通过三个点确定变换的位子
src = np.float32([[400,300] , [800,300] , [400,1000]])  #原先的三个点 (竖着和横着来确定两条直线)
dst = np.float32([[200,400] , [600,500] , [150,1100]])  #现在的三个点
M = cv.getAffineTransform(src , dst)
img_2 = cv.warpAffine(img , M  ,(w,h))


