import cv2
import numpy as np
import time

fileName = './resources/roi.jpg'

img1 = cv2.imread(fileName)
e1 = cv2.getTickCount()
t1 = time.time()
for i in xrange(5, 49, 2):
    img1 = cv2.medianBlur(img1, i)
e2 = cv2.getTickCount()
t2 = time.time()

t = (e2 - e1) / cv2.getTickFrequency()
tt = t2 - t1

print t
print tt