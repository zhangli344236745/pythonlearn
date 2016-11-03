__author__ = '0138695'
import cv2

imgSrc = cv2.imread(r'bio-photo.jpg')
#cv2.imwrite(r'save.png', imgSrc)

capture = cv2.VideoCapture(0)
cv2.namedWindow('Image')
cv2.imshow('Video', imgSrc)
cv2.waitKey(0)

cv2.destroyWindow('Video')