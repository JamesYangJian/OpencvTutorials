import cv2
import numpy as np
import matplotlib.pyplot as plt

src = np.ones([200, 150, 3])

cv2.line(src, (0, 20), (150, 20), (0, 0, 0), 1)
cv2.line(src, (0, 60), (150, 60), (0, 0, 0), 1)
cv2.line(src, (0, 100), (150, 100), (0, 0, 0), 1)
cv2.line(src, (0, 140), (150, 140), (0, 0, 0), 1)
cv2.line(src, (0, 180), (150, 180), (0, 0, 0), 1)

cv2.line(src, (20, 0), (20, 200), (0, 0, 0), 1)
cv2.line(src, (80, 0), (80, 200), (0, 0, 0), 1)
cv2.line(src, (140, 0), (140, 200), (0, 0, 0), 1)

cv2.rectangle(src, (50, 120), (120, 190), (0, 0, 0), 1)

cv2.imshow('test', src)
cv2.waitKey(0)
cv2.destroyAllWindows()



rows, cols, _ = src.shape
pt1 = [40, 50]
pt1_new = [30, 70]
pt2 = [120, 50]
pt2_new = [120, 50]
pt3 = [40, 120]
pt3_new = [70, 140]

cv2.circle(src, tuple(pt1), 2, (0, 255, 0), -1)
cv2.circle(src, tuple(pt2), 2, (0, 255, 0), -1)
cv2.circle(src, tuple(pt3), 2, (0, 255, 0), -1)

pts1 = np.float32([pt1, pt2, pt3])
pts2 = np.float32([pt1_new, pt2_new, pt3_new])

M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(src, M, (cols*2, rows*2))

plt.subplot(121), plt.imshow(src), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()