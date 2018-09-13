import cv2
import numpy as np
import matplotlib.pyplot as plt


file1 = './resources/apple.jpg'
file2 = './resources/orange.jpg'


A = cv2.imread(file1)
B = cv2.imread(file2)

g = A.copy()
gpA = [g]

for i in xrange(1, 6, 1):
    g = cv2.pyrDown(g)
    gpA.append(g)

lpA = [gpA[5]]
for i in xrange(5, 0, -1):
    GE = cv2.pyrUp(gpA[i])
    L = cv2.subtract(gpA[i-1], GE)
    lpA.append(L)

g = B.copy()
gpB = [g]

for i in xrange(1, 6, 1):
    g = cv2.pyrDown(g)
    gpB.append(g)

lpB = [gpB[5]]
for i in xrange(5, 0, -1):
    GE = cv2.pyrUp(gpB[i])
    L = cv2.subtract(gpB[i-1], GE)
    lpB.append(L)

LS = []
for la, lb in zip(lpA, lpB):
    rows, cols, dpt = la.shape
    ls = np.hstack((la[:, 0:cols/2, :], lb[:, cols/2:, :]))
    LS.append(ls)

for i in xrange(len(LS)):
    cv2.imshow('img%s' % (str(i)), LS[i])

cv2.waitKey(0)
cv2.destroyAllWindows()

ls_ = LS[0]
for i in xrange(1, 6):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_, LS[i])

real = np.hstack((A[:, 0:cols/2, :], B[:, cols/2:, :]))

plt.subplot(221)
b, g, r = cv2.split(A)
A = cv2.merge((r, g, b))
plt.imshow(A)
plt.title('Apple')
plt.axis('off')

plt.subplot(222)
b, g, r = cv2.split(B)
B = cv2.merge((r, g, b))
plt.imshow(B)
plt.title('Orange')
plt.axis('off')

plt.subplot(223)
b, g, r = cv2.split(real)
real = cv2.merge((r, g, b))
plt.imshow(real)
plt.title('Orange')
plt.axis('off')

plt.subplot(224)
b, g, r = cv2.split(ls_)
ls_ = cv2.merge((r, g, b))
plt.imshow(ls_)
plt.title('Orange')
plt.axis('off')


plt.show()