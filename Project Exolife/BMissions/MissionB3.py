from PIL import Image
import numpy as np
import os
import sys

hdsurface = Image.open('HD215497.pbm')

pixels = np.array(hdsurface)
#print pixels
maxtemp = 0
temp = 0
nbrows = hdsurface.size[1]
#print nbrows
nblines = hdsurface.size[0]
#print nblines
hdsurfacesplit = np.zeros((nbrows,nblines))
hdsurfacesplit1 = np.zeros((nbrows,nblines))
hdsurfacesplit2 = np.zeros((nbrows,nblines))
hdsurfacesplit3 = np.zeros((nbrows,nblines))
hdsurfacesplit4 = np.zeros((nbrows,nblines))

i=0
j=0

while i<nbrows:
    while j<nblines:
        temp = pixels[i,j]
        if pixels[i,j]<50:
            hdsurfacesplit[i,j]=0;
            hdsurfacesplit1[i,j]=255;
        elif 50<=pixels[i,j]<127:
            hdsurfacesplit[i,j]=85;
            hdsurfacesplit2[i,j]=255;
        elif 127<=pixels[i,j]<230:
            hdsurfacesplit[i,j]=180;
            hdsurfacesplit3[i,j]=255;
        else:
            hdsurfacesplit[i,j]=255;
            hdsurfacesplit4[i,j]=255;

        #print temp
        #print maxtemp
        
        j+=1
    i+=1
    j=0
#print heatriver
hdsplitimg = Image.fromarray(hdsurfacesplit.astype('uint8'))
hdsplitimg1 = Image.fromarray(hdsurfacesplit1.astype('uint8'))
hdsplitimg2 = Image.fromarray(hdsurfacesplit2.astype('uint8'))
hdsplitimg3 = Image.fromarray(hdsurfacesplit3.astype('uint8'))
hdsplitimg4 = Image.fromarray(hdsurfacesplit4.astype('uint8'))
hdsplitimg.show()
hdsplitimg1.show()
hdsplitimg2.show()
hdsplitimg3.show()
hdsplitimg4.show()