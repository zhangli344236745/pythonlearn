import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img  = cv.imread("bio-photo.jpg",0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

fimg = np.log(np.abs(fshift))

plt.subplot(121)
plt.imshow(img,'gray')
plt.title("Origin Fourier")

plt.subplot(122)
plt.imshow(fimg,'gray')
plt.title("Fourier Fourier")

plt.show()


