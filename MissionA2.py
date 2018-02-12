from PIL import Image
import numpy as np
import os
import sys

marssurface = Image.open('Mars_surface.pbm')
#marssurface.show()


#print "Definition = {} px".format(marssurface.size[0]*marssurface.size[1])
#sizebyte = (marssurface.size[0]*marssurface.size[1]*3)
#print "Size in byte is: {}".format(sizebyte)
#sizebytefile = os.path.getsize("/home/william/Desktop/anemona.jpeg")
#print "Actual file size in byte is: {}".format(sizebytefile)
pixels = np.array(marssurface)
#print pixels
percentgaz = 0
gaz = 0
totgaz = 0
totpercentgaz = 0
nbrows = marssurface.size[1]
print nbrows
nblines = marssurface.size[0]
print nblines
i=0
j=0

while i<nbrows:
    while j<nblines:
        #print pixels[i,j]
        gaz = pixels[i,j]
        totgaz = gaz + totgaz
        print gaz
        percentgaz = gaz/2.56
        totpercentgaz = percentgaz + totpercentgaz
        print percentgaz

        j+=1
    i+=1
    j=0
percentgazfin = totpercentgaz/(nblines*nbrows)
print percentgazfin
percentgazfin = (totgaz/2.59)/(nblines*nbrows)
print percentgazfin
