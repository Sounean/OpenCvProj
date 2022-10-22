import numpy as np
import cv2 as cv


img = np.zeros((480,640,3) , np.uint8)

# 画线line
cv.line(img , (10,10) , (300,400) , (0,0,255) , 5)  #画线 （参数1：图片，参数2：开始的坐标，参数3：结束的坐标，参数4：颜色,参数5：线宽5）
cv.line(img , (80,100) , (380,400) , (0,0,255) , 16)    #线越宽越平滑

# 画圆circle
cv.circle(img , (320,240) , 100 , (0,0,255))
cv.circle(img , (320,240) , 5 , (0,0,255) , -1)

# 画椭圆ellipse
#(参数1：图片，参数2：中心点，参数3：长度的一半，参数4：角度，参数5：从哪个角度开始，参数6：到哪个角度结束)  根据参数45可以表示截取部分椭圆(按顺时针计算的，从左边开始计算)
cv.ellipse(img , (330,240) , (100,50) , 0  , 0 , 360 , (0,0,255))

# 画多边形polylines
pts = np.array([(300,10)  , (150,100) , (450,100)] , np.int32)
cv.polylines(img , [pts] , True , (0,0,255))    #true表示矩形闭合

# 填充多边形fillPoly(img，点集，颜色)
cv.fillPoly(img , [pts] , (255,255,0))

# 画文本(图片，字符串，启始点，字体，字号，颜色)
cv.putText(img , 'Hello' , (10,400) , cv.FONT_HERSHEY_PLAIN , 1 , (255,0,0))


cv.imshow('draw',img)
cv.waitKey(0)


