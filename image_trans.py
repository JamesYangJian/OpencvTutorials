import cv2
import numpy as np
import time



img1 = cv2.imread('./resources/opencv.jpg')
img2 = cv2.imread('./resources/blending1.jpg')


weight1 = 0.0
weight2 = 1 - weight1
unit = 0.01

while True:
    img3 = cv2.addWeighted(img1, weight1, img2, weight2, 0)

    cv2.imshow('blend', img3)
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

    weight1 += unit
    weight2 = 1 - weight1
    if weight1 >= 1 or weight1 <= 0:
        unit = -unit
        print 'step changed to %f' % unit





cv2.destroyAllWindows()




