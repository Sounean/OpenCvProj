import cv2 as cv
import numpy as np

cap = cv.VideoCapture('video.mp4')    #加载视频

# bdsubmog = cv.createBackgroudSubtractorMOG()
bdsubmog =cv.createBackgroundSubtractorMOG2()
test = cv.createBackgroundSubtractorMOG2()

while True: #一帧帧获取视频帧
    ret , frame = cap.read()
    if(ret == True):
        cv.cvtColor(frame , cv.COLOR_BGR2GRAY)#灰度化
        blur = cv.GaussianBlur(frame , (15,15) , 1000)   #高斯去噪
        mask = bdsubmog.apply(blur)    #去背景

        t1 = test.apply(frame)

        cv.imshow('video' ,mask)
        cv.imshow('t1', t1)

    key = cv.waitKey(1)
    if(key == 27):  #相当于”esc“键
        break

cap.release()
cv.destroyAllWindows()#释放资源