import cv2 as cv
import numpy as np

img1 = cv.imread('opencv_search.png')   #1.打开图片
img2 = cv.imread('opencv_orig.png')

gray1 = cv.cvtColor(img1 , cv.COLOR_BGR2GRAY)
gray2 = cv.cvtColor(img2 , cv.COLOR_BGR2GRAY)

sitf = cv.SIFT_create() #2.1创建SIFT特征检测器对象

kp1 , des1 = sitf.detectAndCompute(gray1 , None)    #2.2通过sitf对象获得两个图的获取特征点和描述子
kp2 , des2 = sitf.detectAndCompute(gray2 , None)

#创建匹配器
index_params = dict(algorithm = 1 ,trees = 5)
search_params = dict(checks = 50)
flann = cv.FlannBasedMatcher(index_params , search_params)

matchs = flann.knnMatch(des1 , des2 , k=2)#对描述子进行匹配计算


good = []
for i,(m,n) in enumerate(matchs):
    if m.distance <0.7 * n.distance:    #小于一定差距表示是一个不错的匹配点(越小表明要求越高，那么得到的点也就越少)
        good.append(m)


if len(good) >= 4:
    # reshape函数功能为改变数组或矩阵的形状,有几个参数就表示有几个维，-1表示根据后面自动算
    #queryIdx是目标图像的描述符索引 [kp1[m.queryIdx].pt 这样子获取的是(x,y)，且为图片中心点
    srcPts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1 , 1 , 2)
    print(srcPts)
    dstPts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1 , 1 , 2)
    H , _ =  cv.findHomography(srcPts  , dstPts ,cv.RANSAC , 5.0)   #获得单应性矩阵

    h,w = img1.shape[:2]
    pts = np.float32([[-0,0] , [0,h-1] , [w-1,h-1] , [w-1,0]]).reshape(-1,1,2)
    dst = cv.perspectiveTransform(pts , H)

    cv.polylines(img2 , [np.int32(dst)] , True , (0,0,255))
else:
    print("the number of good is less than 4.")
    exit()

ret = cv.drawMatchesKnn(img1 , kp1 , img2 , kp2 ,[good] ,None)

cv.imshow('result' , ret)
cv.waitKey(0)