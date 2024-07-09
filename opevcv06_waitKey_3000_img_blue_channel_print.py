# -*- coding: utf-8 -*-

import cv2
# 要先把圖檔放在同一目錄(桌面)
#小心副檔名 檔案總管-檢視(勾起來)副檔名
img = cv2.imread('mksh.png')
b =  img[:,:,0] #藍色的channel
g =  img[:,:,1]
r =  img[:,:,2]
print(b)
cv2.imshow('opencv06', img)
cv2.waitKey(3000) #等按空白建
#　等三秒沒按按鍵就消失
cv2.destroyAllWindows() #再關視窗



