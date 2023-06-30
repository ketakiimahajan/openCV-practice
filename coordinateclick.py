import cv2

#define a function to display coordinates of the point when clicked on the image
def click_event(event, x, y, flags, params):
   if event == cv2.EVENT_LBUTTONDOWN:
        print('Left Click')
        print(f'({x},{y})')
   
   if event == cv2.EVENT_RBUTTONDOWN:
        print('Right Click')
        print(f'({x},{y})')
 
img = cv2.imread('watch.jpg')

cv2.namedWindow('Point Coordinates')

cv2.setMouseCallback('Point Coordinates', click_event)
     #mouse callback function to display coordinates of points clicked on image

while True:
   cv2.imshow('Point Coordinates',img)
   if cv2.waitKey(100) & 0xFF == ord('m'):
        break

cv2.destroyAllWindows()