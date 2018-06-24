import cv2
import numpy as np
import matplotlib.pyplot as plt

fileName = './resources/opencv.jpg'

BLUE = [255, 0, 0]
img1 = cv2.imread(fileName)

replicate = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT)
reflect_101 = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value = BLUE)

plt.subplot(231).imshow(img1, 'gray')
plt.title('Original')
plt.axis('off')
plt.subplot(232).imshow(replicate, 'gray')
plt.title('Replicate')
plt.axis('off')
plt.subplot(233).imshow(reflect, 'gray')
plt.title('Reflect')
plt.axis('off')
plt.subplot(234).imshow(reflect_101, 'gray')
plt.title('Reflect_101')
plt.axis('off')
plt.subplot(235).imshow(wrap, 'gray')
plt.title('Wrap')
plt.axis('off')
plt.subplot(236).imshow(constant, 'gray')
plt.title('Constant')
plt.axis('off')

plt.show()
