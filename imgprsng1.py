import cv2
img =cv2.imread('image.jpg')
img_h =cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('hsv',img_h)
cv2.imshow('real',img)
cv2.imshow('hue',img_h[:,:,0])
cv2.imshow('sat',img_h[:,:,1])
cv2.imshow('val',img_h[:,:,2])
cv2.waitKey(0)
cv2.destroyAllWindows()