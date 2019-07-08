# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 21:12:31 2019

@author: kunal
"""

import cv2
cap=cv2.VideoCapture(0)

a=1

while True:
    ret,frame=cap.read()
    cv2.imshow(frame)
    
    if cv2.waitKey(1) & 0xFF=='q':
        break

cap.realease()
cv2.destroyAllWindows()
    
    
