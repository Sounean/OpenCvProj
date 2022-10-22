import cv2 as cv

#1.创建VideoWriter为写多媒体文件
fourcc = cv.VideoWriter_fourcc(*'MJPG')
vw = cv.VideoWriter('./out.mp4',fourcc,25,(640,480)) #保存的路径，视频是25帧，分辨率（应该设置成摄像头真实采集到的分辨率,乱填会写不到数据中去）

#新建窗口
cv.namedWindow('video',cv.WINDOW_AUTOSIZE)

#获取设备/本地视频文件的视频  并读取显示
cap = cv.VideoCapture(0)    #0表示是从设备中读取的 直接放视频路径就表示从本地视频中采集视频
# cv.resize('vidro',640,360)  #让其播放是是按照这个来（下面也得放一个，是cv的bug）

while cap.isOpened():   #判断摄像头是否打开
    #从摄像头读取视频帧
    ret,frame = cap.read()  #有两个返回值，第一个表示是否采集到数据（true表示有），第二个是采集到的视频帧
    # cv.resize('vidro',640,360)  #让其播放是是按照这个来
    # cv.imshow('video',frame)    #将采集到的视频帧在窗口中显示
    # 2.写数据到多媒体文件
    vw.write(frame)
    key = cv.waitKey(1) #那这里用0就会卡住（看起来是卡住其实是因为你传0进去就是让他一直等待，自然久一直一张图片了，可以适当放值，自然越小视频看起来越流畅）
    if(key &0xFF == ord('q')):
        break
#释放VideoCapture
cap.release()
#3.释放VideoWriter
vw.release()
cv.destroyAllWindows()
