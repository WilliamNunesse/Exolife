from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps 
import numpy as np 
import matplotlib.pyplot as plt

U2_surface = Image.open('U2_surface.pbm')


U2_surface = U2_surface.filter(ImageFilter.FIND_EDGES())
nblines = U2_surface.size[1]
nbrows = U2_surface.size[0]

i=0
j=0

while i<nbrows:
    while j<nblines:
    	pixels = U2_surface.getpixel((i, j))
        if pixels>190:
        	U2_surface.putpixel((i, j), 0)
        else:
        	U2_surface.putpixel((i, j), 255)
        
        j+=1
    i+=1
    j=0




#U2_surface = U2_surface.filter(ImageFilter.MedianFilter(3))

U2_surface.show()
