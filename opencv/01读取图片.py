import cv2 as cv    #导入cv模块
img =cv.imread('face1.jpg')  # 读取图片
cv.imshow('read_img' , img) # 显示图片 (窗口上显示的名字，要显示的图片)
cv.waitKey(0)   #填0就会一直显示，不为0则当为那么久时就关闭
cv.destroyAllWindows()  #释放资源