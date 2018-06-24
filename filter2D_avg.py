import cv2
import numpy as np
from matplotlib import pyplot as plt

fileName = './resources/opencv.jpg'

img = cv2.imread(fileName)
kernel = np.ones((5,5), np.float32)/25

dst = cv2.filter2D(img, -1, kernel)

plt.subplot(121)
plt.imshow(img)
plt.title('original')
plt.axis('off')

plt.subplot(122)
plt.imshow(dst)
plt.title('destination kernel(5x5)')
plt.axis('off')

plt.show()

kernel = np.ones((3,3), np.float32)/9

dst = cv2.filter2D(img, -1, kernel)
plt.subplot(121)
plt.imshow(img)
plt.title('original')
plt.axis('off')

plt.subplot(122)
plt.imshow(dst)
plt.title('destination kernel(3x3)')
plt.axis('off')

plt.show()


gaussian_kernel = cv2.getGaussianKernel(5, 1)
print gaussian_kernel


