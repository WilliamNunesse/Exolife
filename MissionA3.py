from PIL import Image
import numpy as np
import os
import sys

europasurface = Image.open('Europa_surface.pbm')
#marssurface.show()


#print "Definition = {} px".format(marssurface.size[0]*marssurface.size[1])
#sizebyte = (marssurface.size[0]*marssurface.size[1]*3)
#print "Size in byte is: {}".format(sizebyte)
#sizebytefile = os.path.getsize("/home/william/Desktop/anemona.jpeg")
#print "Actual file size in byte is: {}".format(sizebytefile)
pixels = np.array(europasurface)
#print pixels
heatmin = 255
temp = 0
nbrows = europasurface.size[1]
print nbrows
nblines = europasurface.size[0]
print nblines
heatriver = np.zeros((nbrows,nblines))
i=0
j=0

while i<nbrows:
    while j<nblines:
        #print pixels[i,j]
        temp = pixels[i,j]
        #print temp
        if temp < heatmin:
            heatriver[i,j]=0
            #print heatriver[i,j]
        else:
            heatriver[i,j]= temp
            #print heatriver[i,j]
        j+=1
    i+=1
    j=0
#print heatriver
europheatimg = Image.fromarray(heatriver.astype('uint8'))
europheatimg.show()