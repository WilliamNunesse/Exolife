from PIL import Image
from PIL import ImageFilter
import numpy as np

img1 = Image.open('Gliese 581d.pbm')
img1 = img1.filter(ImageFilter.MedianFilter(3))
pixels1 = np.array(img1)
img2 = Image.open('Gliese 581d V2.pbm')
img2 = img2.filter(ImageFilter.MedianFilter(3))

img1.show()
img2.show()