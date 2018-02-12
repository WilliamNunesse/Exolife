from PIL import Image
import numpy as np
import os
import sys

gliesesurface = Image.open('GD61.pbm')

pixels = np.array(gliesesurface)
#print pixels
maxtemp = 0
temp = 0
nbrows = gliesesurface.size[1]
#print nbrows
nblines = gliesesurface.size[0]
#print nblines
glieseclear = np.zeros((nbrows,nblines))
i=0
j=0

while i<nbrows:
    while j<nblines:
        temp = pixels[i,j]
        glieseclear[i,j] = 5.68*temp
        #print temp
        if temp>maxtemp:
            maxtemp = temp
        #print maxtemp
        
        j+=1
    i+=1
    j=0
#print heatriver
glieseclearimg = Image.fromarray(glieseclear.astype('uint8'))
glieseclearimg.show()