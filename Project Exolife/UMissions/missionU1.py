# coding: utf-8

from PIL import Image
from PIL import ImageFilter

import numpy as np 
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import LogNorm
import scipy.signal

def detectionContour(nom,imgMat) :
	if nom == "gradient" : 
		fx = np.array([[-1, 0, 1]])
		fy = np.transpose(fx)
	elif nom == "prewitt" : 
		fx = np.array([[-1, 0, 1],[-1, 0, 1],[-1, 0, 1]])
		fy = np.transpose(fx)
	elif nom == "roberts" : 
		fx = np.array([[0, 0, 0],[0, 0, 1],[0, -1, 0]])
		fy = np.array([[0, 0, 0],[0, -1, 0],[0, 0, 1]])
	elif nom == "sobel" :
		fx = np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])
		fy = np.transpose(fx)

	convol_x = scipy.signal.convolve2d(imgMat, fx, mode = 'same')
	convol_y = scipy.signal.convolve2d(imgMat, fy, mode = 'same')
	convol = np.sqrt(convol_x**2 + convol_y**2)

	fig = plt.figure()

	ax1 = fig.add_subplot(2, 2, 1)
	plt.title('Image')
	ax1.imshow(imgMat, cmap = mpl.cm.gray)

	ax2 = fig.add_subplot(2, 2, 2)
	plt.title(nom)
	ax2.imshow(convol, cmap = mpl.cm.gray, norm=LogNorm())

	ax3 = fig.add_subplot(2, 2, 3)
	plt.title('x')
	ax3.imshow(abs(convol_x), cmap = mpl.cm.gray, norm=LogNorm())

	ax4 = fig.add_subplot(2, 2, 4)
	plt.title('y')
	ax4.imshow(abs(convol_y), cmap = mpl.cm.gray, norm=LogNorm())

	#plt.show()

	return convol

def main() :

	filename = 'missionU1.pbm'

	img = Image.open(filename).convert('L')
	mat = np.array(img)
	
	kernel_ph = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
	kernel_moyenneur = np.ones((3,3))/9
	kernel_gaussien = np.array([[1,2,1],[2,4,2],[1,2,1]])
	kernel_rehausseur = np.array([[-1/6,-2/3,-1/6],[-2/3,13/3,-2/3],[-1/6,-2/3,-1/6]])
	kernel_rehausseur /= kernel_rehausseur.sum()
	kernel_laplacien = np.array([[1,1,1],[1,-7,1],[1,1,1]])

	matR = detectionContour('sobel', mat)
	imgR = Image.fromarray(matR.astype('uint8'))
	imgR = imgR.filter(ImageFilter.MedianFilter(3))
	imgR.show()


main()
