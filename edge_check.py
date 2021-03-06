import cv2
import numpy as np
from matplotlib import pyplot as plt

def dir_threshold(img, sobel_kernel=3, thresh=(0, np.pi/2)):

    # Apply the following steps to img
    # 1) Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # 2) Take the gradient in x and y separately
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=sobel_kernel)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=sobel_kernel)
    # 3) Take the absolute value of the x and y gradients
    abs_sobelx = np.absolute(sobelx)
    abs_sobely = np.absolute(sobely)
    # 4) Use np.arctan2(abs_sobely, abs_sobelx) to calculate the direction of the gradient
    absgraddir = np.arctan2(abs_sobely, abs_sobelx)
    # 5) Create a binary mask where direction thresholds are met
    binary_output = np.zeros_like(absgraddir)
    binary_output[(absgraddir > thresh[0]) & (absgraddir <= thresh[1])] = 1
    # 6) Return this mask as your binary_output image
    return binary_output


file = './resources/opencv.jpg'

img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)

edge = cv2.Canny(img, 10, 100)

plt.subplot(121), plt.imshow(img, 'gray'), plt.title('original'), plt.axis('off')
plt.subplot(122), plt.imshow(edge, 'gray'), plt.title('Canny'), plt.axis('off')
#plt.show()


src = np.zeros((6, 6), np.uint8)
for i in xrange(0, 5):
    for j in xrange(0, 5):
        if i==j:
            src[i,j] = 1

print 'src\n %s' % src

sobelx = cv2.Sobel(src, cv2.CV_64F, 1, 0, ksize=-1)

print 'sobelx\n %s' %sobelx
sobely = cv2.Sobel(src, cv2.CV_64F, 0, 1, ksize=-1)
print 'sobely\n %s' % sobely

edge_grad = np.sqrt(np.square(sobelx) + np.square(sobely))

print 'edge_grad:\n%s' % (edge_grad)

theta = np.arctan2(np.absolute(sobely), np.absolute(sobelx))

print 'theta:\n%s' % (theta)

edge = cv2.Canny(src, 0, 10000)
print 'Canny:\n%s' % (edge)