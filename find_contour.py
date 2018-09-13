import cv2
import numpy

fileName = './resources/apple.jpg'
img = cv2.imread(fileName)

cv2.imshow('orig', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('gray', imggray)
cv2.waitKey(0)
cv2.destroyAllWindows()


ret, thresh = cv2.threshold(imggray, 120, 255, 0)

cv2.imshow('gray', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

cv2.imshow('contour', img)
while True:
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()