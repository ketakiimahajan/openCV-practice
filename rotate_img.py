import cv2
import numpy as np

img = cv2.imread('watch.jpg')
rotate_90_cw = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
rotate_180 = cv2.rotate(img, cv2.ROTATE_180)
rotate_90_acw = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow('image', img)
cv2.imshow('rotate_90_cw', rotate_90_cw)
cv2.imshow('rotate_180', rotate_180)
cv2.imshow('rotate_90_acw', rotate_90_acw)

# cv2.getRotationMatrix2D(centre, angle(pos=cw, neg=acw), scale) --> cv2.warpAffine() 
# https://www.projectpro.io/recipes/rotate-image-opencv#:~:text=We%20can%20rotate%20a%20given,getRotationMatrix2D()%20function.

cv2.waitKey(0)
cv2.destroyAllWindows()