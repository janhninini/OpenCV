import cv2

vc = cv2.VideoCapture(0)
while(True):
    ret, frame = vc.read()
    cv2.imshow("You're LIVE", frame)
    if cv2.waitKey(1) == 13:
        break
vc.release()
cv2.destroyAllWindows()
