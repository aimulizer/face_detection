# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 21:53:43 2019

@author: kunal
"""

import cv2

video=cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'xvid')

out= cv2.VideoWriter("output.avi",fourcc,20,(640,480))


while True:
    ret,frames=video.read()
    gray = cv2.cvtColor(frames,cv2.COLOR_BGR2GRAY)
    cv2.imshow("firsst",gray)
    cv2.imshow("second",frames)
    out.write(frames)
    if cv2.waitKey(1) & 0xFF== ord('f'):
        break
    
video.release()
out.release()

cv2.destroyAllWindows()

