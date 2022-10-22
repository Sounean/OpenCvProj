import cv2 as cv

def callback():
    pass
cv.namedWindow('color', cv.WINDOW_NORMAL)

img = cv.imread('image01.jpg')

colorspaces = [cv.COLOR_BGR2RGBA , cv.COLOR_BGR2BGRA ,
               cv.COLOR_BGR2GRAY , cv.COLOR_BGR2HSV_FULL ,
               cv.COLOR_BGR2YUV]
cv.createTrackbar('curcolor' , 'color' , 0 , 4, callback)   #trackerbar名字，窗口名字，默认值，长度，callback函数

while True:
    index = cv.getTrackbarPos('curcolor' , 'color') #获取当前值 (trackerbar名字，是哪个窗口的 )
    cvt_img = cv.cvtColor(img , colorspaces[index]) #颜色空间转换API
    cv.imshow('color' , cvt_img)
    key = cv.waitKey(10)
    if key & 0xFF == ord('q'):
        break
cv.destroyAllWindows()