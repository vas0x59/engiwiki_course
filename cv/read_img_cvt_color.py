import cv2


img = cv2.imread("test.png")


cv2.imshow("test", img)

print(img.shape)
print("img[300, 300, :]",img[300, 300, :]) 
print("w:", img.shape[1], "h:", img.shape[0])

cv2.imshow("hsv", cv2.cvtColor(img, cv2.COLOR_BGR2HSV))
cv2.imshow("gray", cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))

cv2.waitKey(0)
