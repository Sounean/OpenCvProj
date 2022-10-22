#基本功能：
# 可以通过鼠标进行基本图形的绘制
# 1.可以画线：当用户按下l键，即选择了画线。此时，滑动鼠标即可画线，
# 2.可以画矩形： 当用户按下r键，即可选择画矩形。此时，滑动鼠标即可画矩形。
# 3.可以画圆： 当用户按下c键，即可选择画圆。此时，滑动鼠标即可画圆。

import cv2 as cv
import numpy as np

curshape = 0
startpos = (0,0)
#显示窗口和背景
img = np.zeros((480,640,3) , np.uint8)

# 鼠标回调函数
def mouse_callback(event,x,y,flags,userdata):
    global curshape,startpos
    # print(event,x,y,flags,userdata)
    if (event & cv.EVENT_LBUTTONDOWN == cv.EVENT_LBUTTONDOWN):
        startpos = (x,y)    #鼠标左键摁下时记录起始点
    elif (event & cv.EVENT_LBUTTONUP == cv.EVENT_LBUTTONUP):
        if curshape == 0:
            cv.line(img , startpos , (x,y) , (0,0,255))
        elif curshape == 1:
            cv.rectangle(img , startpos , (x,y) , (0,0,255))
        elif curshape == 2:
            a = (x - startpos[0])
            b = (y - startpos[1])
            r = int((a**2+b**2)**0.5)
            cv.circle(img,startpos,r,(0,0,255))
        else:
            print('error:no shape')

# 创建窗口
cv.namedWindow('drawshape' , cv.WINDOW_NORMAL)

# 设置鼠标回调
cv.setMouseCallback('drawshape' , mouse_callback)

while True:
    cv.imshow('drawshape' , img)
    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('l'):   #line
        curshape = 0
    elif key == ord('r'):   #rectangle
        curshape = 1
    elif key == ord('c'):   #circle
        curshape = 2


cv.destroyAllWindows()