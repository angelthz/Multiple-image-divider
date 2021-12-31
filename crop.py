# Importing Image class from PIL module
from PIL import Image
import PyPDF2
import os
from time import sleep
from progressbar import progressbar


#Ruta donde se encuentran las imagenes a cortar
basePath = "directory"

#Ruta donde se guardaran las imagenes una vez que se hayan cortado
outputPath = ""

#Lista donde se almacena el nombre de cada una de las imagenes leidas en
#el directorio basePath
imageList = []


'''
Funcion que abre una imagen
Para cortar la imagen llama a las funciones cropSideA y cropSideB
'''
def openImages(imageName, pageNum):
	im = Image.open(basePath+imageName,mode="r")
	width, height = im.size
	
	if(im):
		cropSideA(im, pageNum)
		cropSideB(im, pageNum)
	else:
		print ("Error al abrir: "+imageName)
	im.close()
	

'''
Funcion que corta una imagen por la mitad
corta el lado A de la imagen
y la guarda en un nuevo fichero en la ruta especificada el outputPath
'''
def cropSideA(im, pageNum):
	width, height = im.size
	left = 65
	top = 0
	right = 1140
	bottom = 1350

	im1 = im.crop((left, top, right, bottom))
	im1.save( (outputPath+"page"+str(pageNum)+".jpg"),format=None )

'''
Funcion que corta una imagen por la mitad}
corta el lado B de la imagen
y la guarda en un nuevo fichero en la ruta especificada el outputPath
'''
def cropSideB(im, pageNum):
	width, height = im.size
	left = 1140
	top = 0
	right = 2215
	bottom = 1350

	im2 = im.crop((left,top,right,bottom))
	im2.save( (outputPath+"page"+str(pageNum)+"-1.jpg"),format=None )


'''
Lista todas las imagenes del directorio establecido
'''
def listAllImages(imagesPath):
	# List all files in a directory using os.listdir
	for entry in os.listdir(imagesPath):
	    if os.path.isfile(os.path.join(imagesPath, entry)):
	        imageList.append(entry)
	        #totalPages+=1


#funcion main
def main():

	pdf = PyPDF2

	listAllImages(basePath)
	pageNumber=1
	print("Cropping images")
	for image in progressbar(imageList):
		#openImages(image, pageNumber)
		pageNumber+=1
		sleep(0.01)

	imageList.clear()

	listAllImages(outputPath)
	print("Writting images into a new PDF File")
	for image in progressbar(imageList):
		#openImages(image, pageNumber)
		pdf.addPage()
		sleep(0.01)


if __name__ == '__main__':
	main()
