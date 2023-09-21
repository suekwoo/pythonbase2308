# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 18:37:13 2023

@author: family
"""

import cv2 as cv

name = input("이를을 입력 하세요  : ")

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("camera open failed")
    exit()
while True:
    ret, img = cap.read()
    if not ret:
        print ("Can't read camera")
        break
    cv.imshow("pc camera", img)
    if cv.waitKey(1) == ord('c'):
        img_capture = cv.imwrite(name+".png", img)
    if cv.waitKey(1) == ord('q'):
        img_capture = cv.imwrite(name+".png", img)
        break
cap.release()
cv.destroyAllWindows()
