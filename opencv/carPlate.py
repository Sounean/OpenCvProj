import cv2 as cv
import pytesseract
import numpy as np

#1.创建Haar级联器
plate = cv.CascadeClassifier('./haarcascades/haarcascade_russian_plate_number.xml')
#2.导入带车牌的图片
img = cv.imread('chinacar.png')

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

carRects = plate.detectMultiScale(gray , 1.1 , 3)  #检测车牌位子

for (x,y,w,h) in carRects:
    cv.rectangle(img , (x,y) , (x+w,y+h) , (0,0,255) , 2)

#对获取到的车牌进行预处理
#1.提取ROI
roi = gray[y:y+h , x:x+w]   #这里把x:x+w输入成x+x+w导致roi显示不正常仅一小部分
print(roi.shape)

#2.进行二值化
ret , roi_bin = cv.threshold(roi , 0 ,255 , cv.THRESH_BINARY + cv.THRESH_OTSU)
# print(ret)
print(pytesseract.image_to_string(roi , lang='chi_sim+eng' , config='--psm 8 --oem 3'))  #第二个参数这样子中英文都能识别到

cv.imshow('roi_bin' , roi)
cv.imshow('img',img)
cv.waitKey(0)
