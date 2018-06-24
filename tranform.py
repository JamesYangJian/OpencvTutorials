import cv2
import numpy as np

fileName = './resources/opencv.jpg'

img = cv2.imread(fileName)
res = cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)

height, width = img.shape[:2]
print 'height=%d, width=%d' % (height, width)
res1 = cv2.resize(img, (2*width, 2*height), interpolation=cv2.INTER_CUBIC)

while (1):
    cv2.imshow('res', res)
    cv2.imshow('img', img)
    cv2.imshow('res1', res1)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()

fileName = './resources/roi.jpg'
img = cv2.imread(fileName)
rows, cols, _ = img.shape

M = np.float32([[1, 0, 20], [0, 1, 30]])
dst = cv2.warpAffine(img, M, (cols, rows))

merge = np.hstack((img, dst))
cv2.imshow('img', merge)
cv2.waitKey(0)
cv2.destroyAllWindows()


rows, cols, _ = img.shape
M = cv2.getRotationMatrix2D((cols/2, rows/2), 60, 1)

print M

dst = cv2.warpAffine(img, M, (2*cols, 2*rows))
while True:
    cv2.imshow('img', dst)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()