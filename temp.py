# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2

img=cv2.imread('messi.jpg')


face_cascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray_img,scaleFactor = 1.05,minNeighbors = 5)


for  x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)
print(type(faces))
print(faces)

cv2.imshow('legend',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(img.shape)
 
 



