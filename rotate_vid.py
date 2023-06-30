import cv2
import numpy as np

cap = cv2.VideoCapture(0)
k = 0

while True:
    ret, frame = cap.read()
    #k = 0
    if k == 0:
        #ret, frame = cap.read()
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        k = 1
        print(k)
    
    elif k == 1:
        frame = cv2.rotate(frame, cv2.ROTATE_180)
        k = 2
        print(k)
    
    elif k == 2:
        frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
        k = 3
        print(k)
    
    else:
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        cv2.imshow('frame rotated 360', frame)
        print(k)

    if cv2.waitKey(1000) & 0xFF == ord('m'):
        break

cap.release()
cv2.destroyAllWindows()