from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img=Image.open("missionA1.pbm")
mat=np.array(img)

ligne=img.size[1]
colonne=img.size[0]

liste=[]
valeurMax=255

for i in range (ligne-1):
	for j in range (colonne-1):
		valeur=mat[i,j]
		if valeur<valeurMax:
			valeurMax=valeur
			liste=[]
			liste.append((i,j))
		elif valeur==valeurMax:
			liste.append((i,j))

i=0

while i < len(liste):
	print(liste[i])
	i += 1

img.show()
#print("Les coordonnees du point d'atterissage sont : x=%s y=%s" % (xValeurMax, yValeurMax))