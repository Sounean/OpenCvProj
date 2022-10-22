import cv2 as cv
#1.新建窗口
cv.namedWindow('video',cv.WINDOW_AUTOSIZE)

#2.获取设备/本地视频文件的视频  并读取显示
cap = cv.VideoCapture(0)    #0表示是从设备中读取的 直接放视频路径就表示从本地视频中采集视频
while True:
    #从摄像头读取视频帧
    ret,frame = cap.read()  #有两个返回值，第一个表示是否采集到数据（true表示有），第二个是采集到的视频帧
    cv.imshow('video',frame)    #将采集到的视频帧在窗口中显示
    key = cv.waitKey(1) #那这里用0就会卡住（看起来是卡住其实是因为你传0进去就是让他一直等待，自然久一直一张图片了，可以适当放值，自然越小视频看起来越流畅）
    if(key &0xFF == ord('q')):
        break
#3.释放VideoCapture
cap.release()
cv.destroyAllWindows()

