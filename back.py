import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened():
    r, f = cap.read()

    if r:
        cv2.imshow("image", f)

        if cv2.waitKey(5) == ord('q'):
            cv2.imwrite("image.jpg", f)
            break

cap.release()
cv2.destroyAllWindows()
