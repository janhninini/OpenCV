import cv2
cap=cv2.VideoCapture(0)
count=0
while True:
    ret,frame=cap.read()
    if ret:
        cv2.imshow("window",frame)

    key=cv2.waitKey(1)
    if ord('q')==0xff & key:
        break
    if ord('c') == 0xff & key:
        cv2.imwrite("{}.png".format(count),frame)
        count+=1
cap=cv2.release()
cv2.destroyAllWindows()
