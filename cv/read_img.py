import cv2


img = cv2.imread("test.png")


cv2.imshow("test", img)

print(img.shape)
print("img[300, 300, :]",img[300, 300, :]) 
print("w:", img.shape[1], "h:", img.shape[0])
cv2.waitKey(0)
