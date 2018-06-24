import cv2
import numpy as np
from matplotlib import pyplot as plt

#file = './resources/erode_ex.jpg'
file = './resources/erode_outer_noise.jpg'

file_inner = './resources/erode_inner_noise.jpg'

img = cv2.imread(file)
kernel = np.ones((5,5), np.uint8)


erode = cv2.erode(img, kernel, iterations=2)

dilate = cv2.dilate(erode, kernel, iterations=1)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

plt.subplot(421), plt.title('original'), plt.imshow(img, 'gray')
plt.axis('off')

plt.subplot(422), plt.title('erode'), plt.imshow(erode, 'gray')
plt.axis('off')

plt.subplot(423), plt.title('dilate'), plt.imshow(dilate, 'gray')
plt.axis('off')

plt.subplot(424), plt.title('Morphplogy Open'), plt.imshow(opening, 'gray')
plt.axis('off')

img = cv2.imread(file_inner)
kernel = np.ones((11,11), np.uint8)
close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

dilate = cv2.dilate(img, kernel, iterations=1)
erode = cv2.erode(dilate, kernel, iterations=1)

plt.subplot(425), plt.title('Inner Noise'), plt.imshow(img, 'gray')
plt.axis('off')

plt.subplot(426), plt.title('Dilate Inner Noise'), plt.imshow(dilate, 'gray')
plt.axis('off')

plt.subplot(427), plt.title('Erode Inner noise'), plt.imshow(erode, 'gray')
plt.axis('off')

plt.subplot(428), plt.title('Morphplogy close'), plt.imshow(close, 'gray')
plt.axis('off')

plt.show()

