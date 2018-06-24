import cv2
import matplotlib.pyplot as plt
import numpy as np

file = './resources/adapt_thresh.jpg'
file = './resources/opencv.jpg'
#file = './resources/chess.jpg'


img = cv2.imread(file, cv2.IMREAD_ANYCOLOR)
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

laplacian = cv2.Laplacian(img, cv2.CV_64F)
abs_lap = np.absolute(laplacian)

sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
abs_sobelx = np.absolute(sobel_x)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
abx_sobely = np.absolute(sobel_y)
plt.subplot(221), plt.imshow(img, 'gray'), plt.title('Original'), plt.axis('off')
plt.subplot(222), plt.imshow(abs_lap, 'gray'), plt.title('Laplacian'), plt.axis('off')
plt.subplot(223), plt.imshow(abs_sobelx, 'gray'), plt.title('Sobel X'), plt.axis('off')
plt.subplot(224), plt.imshow(abx_sobely, 'gray'), plt.title('Sobel Y'), plt.axis('off')

plt.show()

file = './resources/box.jpg'
img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)

sobelx_8u = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=5)
abs_sobelx_8u = np.absolute(sobelx_8u)

sobelx_64f = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize = 5)
abs_sobelx_64f = np.absolute(sobelx_64f)

laplacian_8u = cv2.Laplacian(img, cv2.CV_8U)
abs_laplacian8u = np.absolute(laplacian_8u)

laplacian_64f = cv2.Laplacian(img, cv2.CV_64F)
abs_laplacian64f = np.absolute(laplacian_64f)

plt.subplot(321), plt.imshow(img, 'gray'), plt.title('Original'), plt.axis('off')
plt.subplot(322), plt.imshow(abs_sobelx_8u, 'gray'), plt.title('SobelX 8U'), plt.axis('off')
plt.subplot(323), plt.imshow(abs_sobelx_64f, 'gray'), plt.title('SobelX 64F'), plt.axis('off')
plt.subplot(324), plt.imshow(abs_laplacian8u, 'gray'), plt.title('Laplacian 8U'), plt.axis('off')
plt.subplot(325), plt.imshow(abs_laplacian64f, 'gray'), plt.title('Laplacian 64F'), plt.axis('off')
plt.show()