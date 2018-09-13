import cv2
import matplotlib.pyplot as plt
import numpy as np


file = './resources/roi.jpg'

img = cv2.imread(file)

x, y = img.shape[0:2]

print x, y


img_pydown_1 = cv2.pyrDown(img)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_pydown_gray = cv2.cvtColor(img_pydown_1, cv2.COLOR_BGR2GRAY)

lap_py = cv2.subtract(img_gray ,cv2.pyrUp(img_pydown_gray))

cv2.imshow('Original', img)
cv2.imshow('Down_1', img_pydown_1)
cv2.imshow('Laplacian_Py', lap_py)

cv2.waitKey(0)
cv2.destroyAllWindows()