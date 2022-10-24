import cv2 as cv
import numpy as np

min_w = 90
min_h = 90
line_high = 560     #检测线的高度
line_offset = 8 #线的偏移量
cars = []   #存放有效车辆数组
carNum = 0  #统计车的数量

def center(x,y,w,h):    #算出中心点
    x1 = int(w/2)
    y1 = int(h/2)
    cx = x+x1
    cy = y+y1
    return cx,cy

cap = cv.VideoCapture('video.mp4')    #加载视频

# bdsubmog = cv.createBackgroudSubtractorMOG()
bdsubmog =cv.createBackgroundSubtractorMOG2()
test = cv.createBackgroundSubtractorMOG2()

#形态学kernel
kernel = cv.getStructuringElement(cv.MORPH_RECT , (5,5))

while True: #一帧帧获取视频帧
    ret , frame = cap.read()
    if(ret == True):
        cv.cvtColor(frame , cv.COLOR_BGR2GRAY)#灰度化
        blur = cv.GaussianBlur(frame , (15,15) , 1000)   #高斯去噪
        mask = bdsubmog.apply(blur)    #去背景

        erode = cv.erode(mask,kernel) #腐蚀 (去斑块用)
        dilate = cv.dilate(erode , kernel , iterations=2) #膨胀
        close = cv.morphologyEx(dilate , cv.MORPH_CLOSE , kernel)   #闭运算 去掉五体内小方块

        cnts , h = cv.findContours(close , cv.RETR_TREE , cv.CHAIN_APPROX_SIMPLE)  #寻找轮框cnts表所有轮廓，h表所有层级

        t1 = test.apply(frame)

        cv.line(frame , (10,line_high) , (1200,line_high) , (255,255,0) , 3)    #画一条检测线
        for(i , c) in enumerate(cnts):
            (x,y,w,h) = cv.boundingRect(c)  #获得x，y，宽和高
            isValid = (w >= min_w) and ( h >= min_h )
            if(not isValid):
                continue
            cv.rectangle(frame , (x,y) , (x+w,y+h) , (0,0,255) , 2)  #画在图片上 #到这里的都是有效的车
            cpoint = center(x,y,w,h)   #求车的中心点
            cars.append(cpoint)

            for(x,y) in cars:   #遍历车的数组，当车的中心点落在线的有效区域内，则将这一条线将车辆从数组中减去
                if((y < line_high + line_offset) and (y>line_high-line_offset)):
                    carNum+=1
                    cars.remove((x,y))
                    print(carNum)


        # cv.imshow('raw', t1) #源图像
        # cv.imshow('video' ,mask)    #背景后
        # cv.imshow('erde_img' , erode)
        # cv.imshow('dilate_img' , dilate)
        cv.putText(frame , "Cars Count:" + str(carNum) , (500,60) , cv.FONT_HERSHEY_PLAIN , 2 , (255,0,0) ,5)
        cv.imshow('video' , frame)

    key = cv.waitKey(1)
    if(key == 27):  #相当于”esc“键
        break

cap.release()
cv.destroyAllWindows()#释放资源