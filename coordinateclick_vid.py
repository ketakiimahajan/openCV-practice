import cv2
import numpy as np

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('Left Click')
        print(f'({x},{y})')
   
    if event == cv2.EVENT_RBUTTONDOWN:
        print('Right Click')
        print(f'({x},{y})')

cap = cv2.VideoCapture(0)

cv2.namedWindow('Point Coordinates') # name of window, should be SAME EVERYWHERE!

cv2.setMouseCallback('Point Coordinates', click_event)

while True:
    ret, frame = cap.read()
    cv2.imshow('Point Coordinates', frame)
    if cv2.waitKey(1) & 0xFF == ord('m'):
        break
cv2.destroyAllWindows()