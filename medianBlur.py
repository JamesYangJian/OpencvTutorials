import cv2
from matplotlib import pyplot as plt

fileName = './resources/opencv_noisy.jpg'

img = cv2.imread(fileName)

blur = cv2.medianBlur(img, 3)

plt.subplot(121)
plt.imshow(img)
plt.title('Original')
plt.axis('off')

plt.subplot(122)
plt.imshow(blur)
plt.title('medianBlur')
plt.axis('off')

plt.show()

fileName = './resources/bilateral_ex.jpg'
img = cv2.imread(fileName)
blur = cv2.bilateralFilter(img, 9, 75, 75)

b, g, r = cv2.split(img)
img = cv2.merge((r, g, b))

b, g, r = cv2.split(blur)
blur = cv2.merge((r, g, b))

plt.subplot(121)
plt.imshow(img)
plt.title('Original')
plt.axis('off')

plt.subplot(122)
plt.imshow(blur)
plt.title('BilateralBlur')
plt.axis('off')

plt.show()