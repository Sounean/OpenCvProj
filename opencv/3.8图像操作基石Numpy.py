import cv2 as cv
import numpy as np

#通过array定义矩阵
# a = np.array([1,2,3])   #一维数组
# b = np.array([[1,2,3] , [4,5,6]])   #两行三列
# print(a)
# print(b)
#
# # 定义zeros矩阵
# c = np.zeros((8,8,3) , np.uint8)    # ((传参1：行个数，传参2：列个数，传参3：通道数/层数（这里写3是因为彩色都是3通道的如果是0那就是灰色的）) ， 传参4：矩阵中的数据类型（表示每个值最大255）)
# print(c)
#
# # 定义ones矩阵
# d = np.zeros((8,8,3) , np.uint8)    # ((传参1：行个数，传参2：列个数，传参3：通道数/层数（这里写3是因为彩色都是3通道的如果是0那就是灰色的）) ， 传参4：矩阵中的数据类型（表示每个值最大255）)
# print(d)
#
# #定义full矩阵
# e = np.full((8,8) , 10 , np.uint8)
# print(e)
#
# #定义单位矩阵identity
# f = np.identity(8)  #   表示是8*8的矩阵
# print(f)
#
# #定义长条矩阵 (对角线为1)
# g = np.eye(5 , 7 , k=3) #表示从第3+1（即4）个开始做对角线
# print(g)


img = np.zeros((480,640,3) , np.uint8)      #第三个参数不填那就是黑白了，填3表示是三个通道
# print(img[100,100]) #检索img中下标为[100,100]的
#
# count = 0
# while count <200:
#     img[count,100,0] = 255
#     # img[count , 100] = [0,0,255]  表示三个图层第一层0第二层0第三层255
#     count = count + 1   #对某个元素赋值

roi = img[100:400 , 100:600]    #把原图裁到（100，100）到（400，600）的大小
# roi[:,:] = [0,0,255]
roi[10:200 , 10:200] = [0,255,0]    #把[10:200 , 10:200]部分的矩形换掉颜色

cv.imshow('img' , roi)
key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyAllWindows()