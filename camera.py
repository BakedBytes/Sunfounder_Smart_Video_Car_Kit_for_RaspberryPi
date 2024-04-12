import cv2

cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# cap.set(cv2.CAP_PROP_FPS, 30)

while True:
    ret, img = cap.read()
    if ret is True:
        cv2.imshow('PiCamera', img)
    else:
        continue
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()