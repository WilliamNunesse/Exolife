from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
import numpy as np

img1=Image.open("missionA4_1.pbm")
img2=Image.open("missionA4_2.pbm")
img1 = img1.filter(ImageFilter.MedianFilter(3))
img2 = img2.filter(ImageFilter.MedianFilter(3))

ligne=img1.size[1]
colonne=img1.size[0]

mat1=np.array(img1)
mat2=np.array(img2)
matF=np.zeros((ligne,colonne))



for i in range (ligne-1):
	for j in range (colonne-1):
		if mat1[i,j]==0 or mat1[i,j]==255:
			matF[i,j]=mat2[i,j]
		else :
			matF[i,j]=mat1[i,j]



imgToDisplay=Image.fromarray(matF.astype('uint8'))
imgToDisplay.show()
