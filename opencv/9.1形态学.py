import cv2 as cv
import numpy as np

img = cv.imread('test01.jpg')
cv.imshow('img' , img)  # 原图
gray_img = cv.cvtColor(img , cv.COLOR_BGR2GRAY)    #设置成灰度图片
# cv.imshow('gray_img' , gray_img)    # 灰度图
kernal = np.ones((19,19) , np.uint8)

# # 全局二值化：cv.threshold(灰度图 , 阈值 , 超过阈值后设置的值 , cv.THRESH_BINARY)
# ret , dst = cv.threshold(gray_img , 180 , 255 , cv.THRESH_BINARY)   #对gray_img灰度图片，高于180的都设置成255.低于的都设置成0，最后二值化
# cv.imshow('bin' , dst)  # 全局二值化的图

# # 自适应阈值  源,最大阈值,自适应阈值算法,类型，邻近区域的大小,C常量：从计算出的平均值或加权平均值中减去
# dst = cv.adaptiveThreshold(gray_img , 255 , cv.ADAPTIVE_THRESH_GAUSSIAN_C
#                                  , cv.THRESH_BINARY , 3 , 0)
# cv.imshow('dst' , dst)

# # 腐蚀  kernal（卷积核越大腐蚀效果越明显） , 腐蚀次数
# img = cv.imread('i.png')
# erode_img = cv.erode(img , kernal , iterations=2)
# cv.imshow('img' , img)
# cv.imshow('erode_img' , erode_img)

# # 膨胀
# img = cv.imread('i.png')
# dilate_img = cv.dilate(img , kernal , iterations=1)
# cv.imshow('img' , img)
# cv.imshow('dilate_img' , dilate_img)


#cv.morphologyEx:

# #开运算 腐蚀+膨胀  去掉噪点  噪点大就用大一点的核
# img = cv.imread('i2.png')
# dst = cv.morphologyEx(img  , cv.MORPH_OPEN , kernal)    #实质就是先腐蚀再膨胀
# cv.imshow('img' , img)
# cv.imshow('dst' , dst)

# #闭运算 膨胀+腐蚀  去掉噪点  噪点大就用大一点的核
img = cv.imread('i3.png')
dst = cv.morphologyEx(img  , cv.MORPH_CLOSE , kernal)
# cv.imshow('img' , img)
# cv.imshow('dst' , dst)

# #形态学梯度
# img = cv.imread('i3.png')
# dst = cv.morphologyEx(img  , cv.MORPH_GRADIENT , kernal)
# cv.imshow('img' , img)
# cv.imshow('dst' , dst)

# #顶帽运算
# img = cv.imread('raw_tophat.png')
# dst = cv.morphologyEx(img  , cv.MORPH_TOPHAT , kernal)
# cv.imshow('img' , img)
# cv.imshow('dst' , dst)


#黑帽运算
# img = cv.imread('raw_tophat.png')
dst = cv.morphologyEx(img , cv.MORPH_BLACKHAT , kernal)
cv.imshow('img' , img)
cv.imshow('dst' , dst)


cv.waitKey(0)