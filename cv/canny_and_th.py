import cv2


img = cv2.imread("demo_cone.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, th = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
canny = cv2.Canny(gray, 50, 255)

cv2.imshow("gray", gray)
cv2.imshow("th", th)
cv2.imshow("canny", canny)

cv2.waitKey(0)
