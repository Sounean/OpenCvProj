#图像轮廓指具有相同颜色(说明不用先二值化，彩色的也行)或强度的连续点的曲线

import cv2 as cv
import numpy as np

img = cv.imread('contours1.png')

# cv.imshow('img' , img)

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY) #将img转换成单通道的gray
ret,binary = cv.threshold(gray , 150 , 255 , cv.THRESH_BINARY)   #二值化
contours , hierarchy = cv.findContours(binary , cv.RETR_TREE , cv.CHAIN_APPROX_SIMPLE) # 轮廓查找
print(contours)
cv.drawContours(img , contours , -1 , (0,0,255) , 1)#绘制轮廓
# cv.imshow('img' , img)

#轮廓周长和面积 （轮廓，是否是闭合轮廓）
# area = cv.contourArea(contours[0])  # 计算面积
# print("area = %d"%(area))
# len = cv.arcLength(contours[0] , True)  #计算周长
# print("周长：%d"%(len))

def drawShape(src , points):
    i=0
    while i<len(points):
        if(i == len(points)-1):
            x,y = points[i][0]
            x1,y1 = points[0][0]
            cv.line(src , (x,y) , (x1,y1) , (0,0,255) , 1)

        else:
            x, y = points[i][0]
            x1, y1 = points[i + 1][0]
            cv.line(src, (x, y), (x1, y1), (0, 0, 255), 1)
        i = i + 1


# #多边形逼近  (轮廓 ， epsilon ， 是否是闭合的轮廓)
# e = 20
# approx = cv.approxPolyDP(contours[0] , e , True)
# drawShape(img , approx)
# cv.imshow('img' , img)

#凸包 （轮廓，顺时针绘制）

#外接矩形 分为最小cv.minAreaRect(轮廓)和最大矩阵boundingRect(
img = cv.imread('hello.png')
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY) #将img转换成单通道的gray
ret,binary = cv.threshold(gray , 150 , 255 , cv.THRESH_BINARY)   #二值化
contours , hierarchy = cv.findContours(binary , cv.RETR_TREE , cv.CHAIN_APPROX_SIMPLE)
r = cv.minAreaRect(contours[1])
box = cv.boxPoints(r)   #仅获取宽高
box = np.int0(box)
cv.drawContours(img , [box] , 0 , (0,0,255) , 12)   #根据点绘制矩形

x,y,w,h = cv.boundingRect(contours[1])
cv.rectangle(img , (x,y) , (x+w,y+h) , (255,0,0) , 2)
cv.imshow('img',img)










cv.waitKey(0)