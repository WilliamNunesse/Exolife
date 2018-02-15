import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from PIL import Image

u2photo = Image.open('U2_surface.pbm')
#pixels = np.array(u2photo)

dx = ndimage.sobel(u2photo, 0)
dy = ndimage.sobel(u2photo, 1)
pixels = np.hypot(dx, dy)
pixels = (255/np.max(pixels))*pixels

#contour = ndimage.sobel(pixels)
print pixels
contourimg = Image.fromarray(pixels.astype('uint8'))
contourimg.show()

#u2img = scipy.misc.imread('U2_surface.pbm')
#u2img = u2img.astype('int32')
#dx = ndimage.sobel