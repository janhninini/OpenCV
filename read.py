import cv2

i = cv2.imread("WP.jpg")
cv2.imshow("photuuu", i)

print(i.shape)

cv2.imwrite("Output.jpg", i)
cv2.imwrite("Output.png", i)

cv2.waitKey(0)
cv2.destroyAllWindows()
