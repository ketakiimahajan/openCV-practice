import cv2
import numpy as np

cap = cv2.VideoCapture(0)

cv2.namedWindow('Track')

def track(x):
    pass
    # print(x)

cv2.createTrackbar('h min ', 'Track', 0, 179, track)
#cv2.createTrackbar('h max ', 'Track', 179, 179, track)

cv2.createTrackbar('s min ', 'Track', 0, 255, track)
#cv2.createTrackbar('s max ', 'Track', 255, 255, track)

cv2.createTrackbar('v min ', 'Track', 0, 255, track)
#cv2.createTrackbar('v max ', 'Track', 255, 255, track)


while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    hmin_pos = cv2.getTrackbarPos('h min ', 'Track')
    smin_pos = cv2.getTrackbarPos('s min ', 'Track')
    vmin_pos = cv2.getTrackbarPos('v min ', 'Track')
    #hmax_pos = cv2.getTrackbarPos('h max ', 'Track')
    #smax_pos = cv2.getTrackbarPos('s max ', 'Track')
    #vmax_pos = cv2.getTrackbarPos('v max ', 'Track')
    
    lower_boun = np.array([hmin_pos, smin_pos, vmin_pos])
    upper_boun = np.array([179, 255, 255])
    
    mask = cv2.inRange(hsv, lower_boun, upper_boun)
    
    res = cv2.bitwise_and(frame, frame, mask = mask)
    
    cv2.imshow('frame', frame) #red = 0, 100, 100
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    #print(f'Hue: {hue_pos} Saturation: {sat_pos} Value: {val_pos}')
    
    if cv2.waitKey(1) & 0xFF == ord('m'):
        break

cv2.destroyAllWindows()