# -*- coding: utf-8 -*-
# Created by 0138695 on 2017/6/1
import cv2

image = cv2.imread("../bio-photo.jpg")
cv2.imshow("faces",image)
print image
print "height: %d pixels" % (image.shape[0])
print "width: %d pixels" % (image.shape[1])
print "channels: %d" % (image.shape[2])
cv2.waitKey(0)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)