import cv2

cap = cv2.VideoCapture(0)
while (1):

    ret, frame = cap.read()
    print(ret)
    cv2.imshow('frame', frame)
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
