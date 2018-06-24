import cv2
import numpy as np

def do_nothing(x):
    pass

fileName = './resources/opencv.jpg'

img = cv2.imread(fileName)

cv2.namedWindow('GaussianBlur')
cv2.createTrackbar('Kernel Size', 'GaussianBlur', 0, 10, do_nothing)
cv2.createTrackbar('Sigma', 'GaussianBlur', 0, 10, do_nothing)

ksize = 5
sigma = 1


while(1):
    blur = cv2.GaussianBlur(img, (ksize, ksize), sigma)
    cv2.imshow('GaussianBlur', blur)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    ksize = cv2.getTrackbarPos('Kernel Size', 'GaussianBlur')
    ksize = 2*ksize + 1
    sigma = cv2.getTrackbarPos('Sigma', 'GaussianBlur')

    print 'ksize:%d sigma:%d' % (ksize, sigma)

cv2.destroyAllWindows()