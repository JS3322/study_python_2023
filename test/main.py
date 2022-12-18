import cv2

image1 = cv2.imread("1.png",cv2.IMREAD_COLOR)
image2 = cv2.imread("1.png",cv2.IMREAD_GRAYSCALE)
image3 = cv2.imread("1.png",cv2.IMREAD_UNCHANGED)



cv2.imshow("TEST1", image1)
cv2.imshow("TEST2", image2)
cv2.imshow("TEST3", image3)

cv2.waitKey(0)


cv2.destroyAllWindows()
