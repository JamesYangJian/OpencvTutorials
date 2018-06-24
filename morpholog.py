import cv2
import numpy as np
from matplotlib import pyplot as plt


file = './resources/morph.jpg'

img = cv2.imread(file)

kernel = np.ones((9,9), np.uint8)

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
dilate = cv2.morphologyEx(img, cv2.MORPH_DILATE, kernel)
erode = cv2.morphologyEx(img, cv2.MORPH_ERODE, kernel)
subsidy = dilate - erode

img = cv2.imread(file)
top_hat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

black_hat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

plt.subplot(321), plt.imshow(img, 'gray'), plt.title('Original'), plt.axis('off')
plt.subplot(322), plt.imshow(gradient, 'gray'), plt.title('Morpho Gradient'), plt.axis('off')
plt.subplot(323), plt.imshow(subsidy, 'gray'), plt.title('Subtract'), plt.axis('off')
plt.subplot(324), plt.imshow(top_hat, 'gray'), plt.title('TopHat'), plt.axis('off')
plt.subplot(325), plt.imshow(black_hat, 'gray'), plt.title('BlackHat'), plt.axis('off')


plt.show()