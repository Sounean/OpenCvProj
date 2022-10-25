
import cv2 as cv
import numpy as np

img = cv.imread('chess.png')
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

orb = cv.ORB_create()

kp,des = orb.detectAndCompute(gray , None)

cv.drawKeypoints(gray , kp , img)

cv.imshow('ORB' , img)
cv.waitKey(0)