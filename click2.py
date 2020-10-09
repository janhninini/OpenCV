import cv2
cap = cv2.VideoCapture(0)
count = 0
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    crop = gray[:300, :300]
    if ret:
        cv2.imshow("window", gray)
        cv2.imshow("crop", crop)
    key = cv2.waitKey(1)
    if ord('q') == 0xff & key:
        break
    if ord('c') == 0xff & key:
        cv2.imwrite("{}.png".format(count), frame)
        count += 1
cap.release()
cv2.destroyAllWindows()