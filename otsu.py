import cv2 
import numpy as np
from matplotlib import pyplot as plt


fileName = './resources/noisy.jpg'

img = cv2.imread(fileName)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

blur = cv2.GaussianBlur(img, (5, 5), 0)

ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

imgs = [img, 0, th1, img, 0, th2, blur, 0, th3]
titles = ['Original', 'Histogram', 'Global Thresholding',
          'Original', 'Histogram', "Otsu's Thresholding",
          'Gaussian', 'Histogram', "Otsu's Thresholding"]

for i in xrange(3):
    plt.subplot(3, 3, i*3+1), plt.imshow(imgs[i*3], 'gray')
    plt.title(titles[i*3]), plt.axis('off')
    plt.subplot(3, 3, i*3+2),plt.hist(imgs[i*3].ravel(), 256)
    plt.title(titles[i*3+1])#plt.axis('off')
    plt.subplot(3, 3, i*3+3), plt.imshow(imgs[i*3+2], 'gray')
    plt.title(titles[i*3+2]), plt.axis('off')
plt.show()