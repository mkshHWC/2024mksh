# -*- coding: utf-8 -*-
import cv2

img = cv2.imread('RGB.jpg')
img = cv2.resize(img, (256,256))


img1 = cv2.applyColorMap(img, cv2.COLORMAP_PINK)
img2 = cv2.applyColorMap(img, cv2.COLORMAP_HOT)
img3 = cv2.applyColorMap(img, cv2.COLORMAP_HSV)

cv2.imshow("RGB", img)
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("img3", img3)

cv2.waitKey(0)
cv2.destroyAllWindows()
