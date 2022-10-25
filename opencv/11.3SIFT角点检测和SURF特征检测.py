#SIFT步骤：1.创建SIFT对象，2.进行检测:sift.detect(... 3.绘制关键点:drawKeypoints(gray,kp,img)
# 关键点：位置、大小和方向
# 描述子：记录了关键点周围对其有贡献的像素点的一组向量值，其不受仿射变换、光照变换等影响   (用来特征检测)
import cv2 as cv
import numpy as np

img = cv.imread('chess.png')
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

## sitf = cv.xfeatures2d.SIFT_create() #SIFT在扩展包中,老版本可能需要额外引入，4.4.0以上直接用下面那行api即可
# sitf = cv.SIFT_create() #创建SIFT对象
surf = cv.xfeatures2d.SURF_create() #创建SURF对象

# kp ,des = sitf.detectAndCompute(gray , None)    #获取关键点和描述
kp, des = surf.detectAndCompute(gray, None)
print(des)
# sitf.drawKeypoints(gray , kp , img)   #AttributeError: 'cv2.SIFT' object has no attribute 'drawKeypoints'
for marker in kp:
    img = cv.drawMarker(img , tuple(int(i)for i in marker.pt) , color=(0,255,0))

cv.imshow('SIFT' , img)
cv.waitKey(0)