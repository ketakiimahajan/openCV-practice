import cv2
import numpy as np

cap = cv2.VideoCapture(0)
k = 0
#c = 100

while True:
    ret, frame = cap.read()
    
    if k == 0:
        #ret, frame = cap.read()
        frame_hor = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        frame_ver = cv2.rotate(frame, cv2.ROTATE_180)
        k = 1
            
    else:
        frame_hor = cv2.rotate(frame_hor, cv2.ROTATE_180)
        cv2.imshow('frame rotated hor', frame_hor)
        frame_ver = cv2.rotate(frame_ver, cv2.ROTATE_180)
        cv2.imshow('frame rotated ver', frame_ver)

    if cv2.waitKey(100) & 0xFF == ord('m'):
        break

cap.release()
cv2.destroyAllWindows()