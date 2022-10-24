#是Harris检测的微调   (Harris需要根据经验对k进行调整，Shi-Tomasi可以不用对k专门考虑应该设什么最佳)
import cv2 as cv
import numpy as np

blockSize = 2
ksize = 3
k = 0.04
img = cv.imread('chess.png')






cv.waitKey(0)
