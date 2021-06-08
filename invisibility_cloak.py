import cv2
import numpy as np

cap = cv2.VideoCapture(0)
image = cv2.imread("image.jpg")

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#        red = np.unit8([[[0,0,255]]])
#        hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
#        print(hsv_red)
#        cv2.imshow("hsv_red", hsv_red)

        l_red = np.array([0, 100, 100])
        u_red = np.array([10, 255, 255])

        mp1 = cv2.inRange(hsv, l_red, u_red)

        # cv2.imshow("red", mp)

        p1 = cv2.bitwise_and(image, image, mask=mp1)
        # cv2.imshow("p1", p1)
        mp2 = cv2.bitwise_not(mp1)

        p2 = cv2.bitwise_and(frame, frame, mask = mp2)

        cv2.imshow("cloak", p1+p2)

        if cv2.waitKey(5) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
