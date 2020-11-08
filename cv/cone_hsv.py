import cv2
import numpy as np

img = cv2.imread("demo_cone.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv", hsv)
min_o = np.array([0, 61, 118])
max_o = np.array([13, 230, 255])
mask = cv2.inRange(hsv, min_o, max_o)
cv2.imwrite("mask.png", mask)
cv2.imshow("mask", mask)
cv2.waitKey(0)
