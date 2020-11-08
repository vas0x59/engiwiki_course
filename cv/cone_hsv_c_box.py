import cv2
import numpy as np

img = cv2.imread("demo_cone.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv", hsv)
min_o = np.array([0, 61, 118])
max_o = np.array([13, 230, 255])
mask = cv2.inRange(hsv, min_o, max_o)

cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)[-2]
cnts = [i for i in cnts if cv2.contourArea(i) > 10]

out = img.copy()

cv2.drawContours(out, cnts, -1, (0, 255, 0), 2)
for cnt in cnts:
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(out,(x,y),(x+w,y+h),(0,0,255),2)
cv2.imwrite("out.png", out)
cv2.imshow("mask", mask)
cv2.imshow("out", out)
cv2.waitKey(0)
