
import cv2 as cv
from cv2 import dnn
import numpy as np

#1.导入模型，创建神经网络
#2.读图片，转成张量
#3.将张量输入到网络中，并进行预测
#4，得到结果，显示

#导入模型，创建神经网络
config = "./model/bvlc_googlenet.prototxt"
model = "./model/bvlc_googlenet.caffemodel"
net = dnn.readNetFromCaffe(config , model)

#读取图片，转成张量
blob = dnn.blobFromImage(img ,
                  1.0 , #缩放因子
                  (224,224),
                  (104,117,123))

#将张量输入到网络中，并进行预测
net.setInput(blob)
r = net.forward()   #r是一个分类后的结果

#读入类目
