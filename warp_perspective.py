import cv2
import numpy as np
import matplotlib.pyplot as plt

fileName = './resources/timg.jpg'

img = cv2.imread(fileName)
rows, cols, _ = img.shape
img_new = cv2.resize(img, (cols/3, rows/3), interpolation=cv2.INTER_CUBIC)
pt_idx = 0
pts = []

def point_pic(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img_new, (x, y), 3, (0, 255, 0), -1)
        pts.append([x, y])
        print 'Point Number is :%d' %(len(pts))

cv2.namedWindow('img')
cv2.setMouseCallback('img', point_pic)

while True:
    cv2.imshow('img', img_new)

    if len(pts) == 4:
        pts1 = np.float32(pts)
        pts2 = np.float32([[0,0], [300, 0], [0, 300], [300, 300]])
        M = cv2.getPerspectiveTransform(pts1, pts2)
        b, g, r = cv2.split(img_new)
        img_rgb = cv2.merge((r, g, b))
        dst = cv2.warpPerspective(img_rgb, M, (300, 300))

        plt.subplot(121)
        plt.imshow(img_rgb)
        plt.title('Input')

        plt.subplot(122)
        plt.imshow(dst)
        plt.title('output')

        plt.show()
        break


    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()


