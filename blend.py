import cv2
import numpy as np
import matplotlib.pyplot as plt


img1 = cv2.imread('./resources/blending1.jpg')
img2 = cv2.imread('./resources/opencv.jpg')


img3 = img1 + img2

plt.subplot(231).imshow(img1, 'gray')
plt.title('Origin1')
plt.axis('off')

plt.subplot(232).imshow(img2, 'gray')
plt.title('Origin2')
plt.axis('off')

plt.subplot(233).imshow(img3, 'gray')
plt.title('Plus Directly')
plt.axis('off')

img4 = cv2.add(img1, img2)
plt.subplot(234).imshow(img4, 'gray')
plt.title('Cv2 Add')
plt.axis('off')

img5 = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
plt.subplot(235).imshow(img5, 'gray')
plt.title('Cv2 addWeighted')
plt.axis('off')

plt.show()

