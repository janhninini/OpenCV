import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

if cap.isOpened():
    ret, frame = cap.read()
else:
    ret = False

img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
grey_img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

plt.imshow(grey_img1)
plt.show()

plt.imshow(img1)
plt.title("ME")
plt.xticks([])
plt.yticks([])
plt.show()
cap.release()


