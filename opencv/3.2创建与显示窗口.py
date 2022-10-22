import cv2

cv2.namedWindow("new",cv2.WINDOW_AUTOSIZE) #新建一个名为new的窗口
cv2.resizeWindow('new',640,480)
cv2.imshow('new',0) #显示窗口
key = cv2.waitKey(1000)  # 窗口显示时长(单位ms)
if(key == 'q'):
    exit()  # 敲q键退出
cv2.destroyAllWindows() # 销毁窗口

