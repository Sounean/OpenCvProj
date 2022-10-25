#1.标记背景  2.标记前景  3.标记未知域  4.进行分割
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('coins.png')
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

ret,thresh = cv.threshold(gray , 0 ,255 , cv.THRESH_BINARY_INV + cv.THRESH_OTSU)   #二值化,第四个参数填这个就可以让自适应一个阈值，第二个参数可以填0


#开运算去除噪点
kernel = np.ones((3,3) , np.int8)
open1 = cv.morphologyEx(thresh , cv.MORPH_OPEN , kernel , iterations=2)

#膨胀
bg = cv.dilate(open1 , kernel , iterations=1)

#获取前景物体
dist = cv.distanceTransform(open1 , cv.DIST_L2  , 5)   #获得非邻点到离他最近的邻点的距离
ret , fg = cv.threshold(dist , 0.7*dist.max() , 255 , cv.THRESH_BINARY)#此时已经有颜色的变化了，硬币中间亮外边淡，但是需要继续把周围去掉  第二个参数表示超过了最大值0.7倍以上的

#获取未知区域
fg = np.uint8(fg)
unknow = cv.subtract(bg , fg )   #获取未知区域

#创建连通域
ret , marker = cv.connectedComponents(fg)

marker = marker +1  #不加的话个别线可能没有了，加个1对前景基本没影响
marker[unknow == 255] = 0   #未知区域设成0

#进行图像分割
result = cv.watershed(img , marker)

img[result == -1] = [0,0,255]

cv.imshow("img" , img)

cv.imshow('unknow' , unknow)

cv.imshow('ft' , fg)    # 此时一定可以确定前景图中的小圆肯定就是银币
# plt.imshow(dist , cmap='gray')  #不加第二个参数显示的是彩色的，和imshow方式不一致
# plt.show()

# cv.imshow("dist" , dist)
#
# cv.imshow("bg" , bg)
# cv.imshow('thresh' , thresh)






cv.waitKey(0)