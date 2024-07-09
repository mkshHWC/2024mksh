# -*- coding: utf-8 -*-
import cv2
cap = cv2.VideoCapture(0) #數字對應幾號鏡頭

while True:
    ret, img = cap.read()
    cv2.imshow('opencv08', img)
    if cv2.waitKey(33)==27: 
    # 1000 ms 1秒
    #33對應 1/30秒(每秒30張)
        break #27對應esc鍵
    
cv2.destroyAllWindows()
    
    