import cv2 as cv
import numpy as np

#方盒滤波 :
# 当normalize == true时，因为 a=1/（w*H） ， 所以此时方盒滤波==均值滤波

img = cv.imread('test02.png')

# kernel = np.ones((5,5) , np.float32) / 25   #一个每个元素均是1/25的5*5的矩阵
dst = cv.blur(img , (5 , 5))    #卷积后的输出图像
# cv.imshow('img' , img)
# cv.imshow('dst' , dst)



#高斯滤波 (化成曲线的话，每条线都是两边低，中间高,即越靠中间权重越高（而不是值，值肯定比旁边低，但权重肯定比旁边高）)
# ( img,kernal , sigmaX:x的误差 ，sigmaY:y的误差)  不同sigma值，平滑程度不一样，sigma越高越糊
gaussian_dst = cv.GaussianBlur(img , (5 , 5) , sigmaX=1)
# cv.imshow('gaussian_dst' , gaussian_dst)


#中值滤波：用一个数组中取中间值作为卷积后的结果值，就是中值滤波,优点是对椒盐噪点(像胡椒一样小黑点)效果明显
test03 = cv.imread('test03.png')
median_dst = cv.medianBlur(test03 , 5)
# cv.imshow('test03' , test03)
# cv.imshow('median_dst' , median_dst)


#双边滤波： 优点：可以保留边缘，同时可以对边缘内的区域进行平滑处理
bilateral_dst = cv.bilateralFilter(img , 7,20,50)
# cv.imshow('bilateral_dst',bilateral_dst)
# cv.imshow('img' , img)

#高通滤波
# # A.索贝尔算子：cv.Sobel(img源 ， 输出的位深 ， dx(对谁求导,若x为1则检测出y来，即拿到y的边缘，反之亦然) , dy ,ksize(kernal的大小) = 3)
# #Sobel(索贝尔)（高斯）;Scharr(沙尔);Laplacian(拉普拉斯)
# img = cv.imread('chess.png')
# sobel_gety_img = cv.Sobel(img ,cv.CV_64F ,1 ,0 ,ksize=5)    #索贝尔算子y方向边缘 此处x为1，y为0，即拿到y的方向
# sobel_getx_img = cv.Sobel(img ,cv.CV_64F ,0 ,1 ,ksize=5)    #索贝尔算子x方向边缘
# dst1 = cv.add(sobel_gety_img , sobel_getx_img)
# dst2 = cv.Sobel(img ,cv.CV_64F ,1 ,1 ,ksize=5)
# cv.imshow('img' , img)
# cv.imshow('sobel_getY_img' , sobel_gety_img)
# cv.imshow('sobel_getx_img' , sobel_getx_img)
# cv.imshow('dst1' , dst1)
# cv.imshow('dst2' , dst2)    #通过dst1和dst2的对比，可以知道直接对x和y方向进行求导效果极差，所以一般都是先对x求导再是对y求导，最后相加效果最好

# # B.Scharr算子与Sobel类似，只不过使用的kernal值不同,Scharr只能求x方向或者y方向的边缘(Sobel可以同时对xy求边缘，只是效果差，Scharr直接不能)
# img = cv.imread('chess.png')
# d1 = cv.Scharr(img , cv.CV_64F , 1,0)
# d2 = cv.Scharr(img , cv.CV_64F , 0,1)
# dst = cv.add(d1,d2)
# cv.imshow('dst' , dst)

# # C.拉普拉斯算子 可以同时求两个方向的边缘，对噪音敏感，一般需要先进行降噪再调用拉普拉斯
# img = cv.imread('chess.png')
# laplacian_dst = cv.Laplacian(img , cv.CV_64F , ksize=5)
# cv.imshow('img' , img)
# cv.imshow('laplacian_dst' , laplacian_dst)

#边缘检测Canny  (使用简单，效果好)
# 先用了5*5高斯滤波消除噪音。再计算图像梯度方向，再取局部最大值。最后进行阈值计算
# Canny(源 ， 最小的阈值 ， 最大的阈值)
img = cv.imread('chess.png')
cv.imshow('img' , img)
canny_img = cv.Canny(img , 100 , 200)
cv.imshow('canny_img' , canny_img)
















































cv.waitKey(0)