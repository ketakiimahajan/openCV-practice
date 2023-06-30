import cv2
import numpy as np

# select a specific value within a rangeby sliding a slider

cv2.namedWindow('Track')

def track(x):
    pass
    # print(x)

cv2.createTrackbar('x ', 'Track', 0, 100, track)
cv2.createTrackbar('y ', 'Track', 0, 10, track)

while True:
    x_pos = cv2.getTrackbarPos('x ', 'Track')
    y_pos = cv2.getTrackbarPos('y ', 'Track')
    
    print(f'x position: {x_pos} y position: {y_pos}')
    
    if cv2.waitKey(1) & 0xFF == ord('m'):
        break

cv2.destroyAllWindows()

#https://www.youtube.com/watch?v=WUFJu-rJNdQ&ab_channel=AIOCallinonecode