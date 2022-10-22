import cv2 as cv

cv.namedWindow('img',cv.WINDOW_NORMAL)


# A.加载显示图片
faceimg = cv.imread('face1.jpg')    #也可以用直接路径：D:\\uuu\\xxx.jpg
while True: #因为不一直放循环其实不管输入什么都会退出
    cv.imshow('img',faceimg)    # （要放置的窗口名，图片对象）
    key =cv.waitKey(0)
    if(key & 0xFF == ord('q')):    #ord()意思把q转换成asc2码，因为电脑从键盘上获取到的都是asc2码形式（又因为应该asc2码仅取8位所以&0xFF）的
        break
    elif(key &0xFF == ord('s')):
        cv.imwrite("F:\\pythonProject2\\opencv\\123.png" , faceimg) #（要保存的路径（甚至连格式否能帮忙转了），要保存的图片）
cv.destroyAllWindows()