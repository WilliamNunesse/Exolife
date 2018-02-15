from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os
import sys

hdsurface = Image.open('Europa_surface.pbm')

pixels = np.array(hdsurface)
#print pixels
maxtemp = 0
temp = 0
nbrows = hdsurface.size[1]
#print nbrows
nblines = hdsurface.size[0]
#print nblines
#hdsurfacesplit = np.zeros((nbrows,nblines))

unique, counts = np.unique(hdsurface, return_counts=True)
plt.hist(hdsurface, normed=1)
print counts
plt.show()