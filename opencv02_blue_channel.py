# -*- coding: utf-8 -*-
import cv2

img = cv2.imread('onepiece.png')
b = img[:,:,0] #冒號,冒號,0 藍色


cv2.imshow('opencv02', img)
cv2.imshow('blue',b)
cv2.waitKey(0) #K要大寫
#果如果挑任意視窗,按下任意鍵
cv2.destroyAllWindows() # 要把全部的視窗都關閉
