# -*- coding: utf-8 -*-
import cv2

img = cv2.imread('onepiece.png')
#讀入onepiece這張圖,小心副檔名
cv2.imshow('one',img) #要在one秀圖
cv2.imshow('two',img)
cv2.imshow('three',img)
cv2.waitKey(0) #等待任意鍵,卡住,不要結束
#File-New Ctrl-N開新檔案
#File-Save As 另存新檔 
#存[桌面] 的 opencv01.py
#圖還沒放先不執行,不然會當
#圖也要放同一個目錄[桌面]
