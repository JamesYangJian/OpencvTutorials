import cv2
import numpy as np
import matplotlib.pyplot as plt

fileName = './resources/avg_thresh.jpg'

"""
img = cv2.imread(fileName)
ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Orginal', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
imgs = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(0, len(imgs)):
    plt.subplot(2, 3, i+1)
    plt.imshow(imgs[i])
    plt.title(titles[i])
    plt.axis('off')

plt.show()

cv2.waitKey(0)
"""

fileName = './resources/adapt_thresh.jpg'
img = cv2.imread(fileName)
b, g, r = cv2.split(img)
img = cv2.merge((r, g, b))
#img = cv2.medianBlur(img, 3)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 5)

print th3.shape

titles = ['Orignal', 'BINARY', 'MEAN', 'GAUSSIAN']
imgs = [img, th1, th2, th3]

for i in range(0, len(imgs)):
    plt.subplot(2, 2, i+1)
    plt.imshow(imgs[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.show()