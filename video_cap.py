import numpy as np
import cv2
import sys
import time


file_name = './resources/output.avi'
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print 'File can not be opened!'
    sys.exit(0)

w = cap.get(3)
h = cap.get(4)
print 'h is %d, w is %d' % (h, w)

"""
fourcc = cv2.cv.CV_FOURCC('D', 'I', 'V', 'X')
# If I use fourcc as DIVX, the video file will be empty, maybe encoder not be installed
out = cv2.VideoWriter(file_name, 1, 25.0, (640, 480), 1)

while True:
    ret, frame = cap.read()

    if ret:
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.flip(frame, 1)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, 'James', (10, 100), font, 1, (0,0,255), 2 )
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
"""

cap = cv2.VideoCapture(file_name)
if not cap.isOpened():
    print 'Video File can not be opened!'
    sys.exit(0)

last_frame = None
while True:
    ret, frame = cap.read()
    if ret:
        last_frame = frame
        cv2.imshow(file_name, frame)
        if cv2.waitKey(40) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()


cv2.imshow('test', last_frame)
cv2.waitKey(0)
cv2.imwrite('./test.jpg', last_frame)
cv2.destroyAllWindows()