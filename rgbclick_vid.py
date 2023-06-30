# BGR (reverse coordinates)
import cv2
import numpy as np

#define a function to display coordinates of the point when clicked on the image
def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        #print('Left Click')
        #print(f'({x},{y})')
        px = frame[x, y]
        print(px)
    
    if event == cv2.EVENT_RBUTTONDOWN:
        #print('Right Click')
        #print(f'({x},{y})')
        px = frame[x, y]
        print(px)

cap = cv2.VideoCapture(1)

cv2.namedWindow('rgb values')

cv2.setMouseCallback('rgb values', click_event)
    #mouse callback function to display coordinates of points clicked on image

while True:
    ret, frame = cap.read()
    cv2.imshow('rgb values', frame)
    if cv2.waitKey(1) & 0xFF == ord('m'):
        break
cv2.destroyAllWindows()

cv2.destroyAllWindows()