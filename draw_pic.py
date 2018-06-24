import numpy as np
import cv2


file_name = './resources/test.jpg'

img = cv2.imread(file_name)
cv2.line(img, (10, 10), (100,200), (0, 255,255), 5)
cv2.ellipse(img, (400, 320), (100, 50), 0, 90, 270, 255, -1)
cv2.imshow('test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()