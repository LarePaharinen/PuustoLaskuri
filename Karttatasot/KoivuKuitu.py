from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
import functools as ft

sqrSize = 64
i = Image.open("D:\\Vapaa-aika\\Koodaus\\PaikkaTietoikkunaRuutuLaskuri\\images\\Akaa\\koivuKuitu.png")


def countPixels(imgaeArray):

	orangePx = 0
	beigePx = 0
	lightGreenPx = 0
	greenPx = 0
	darkGreenPx = 0
	lightBluePx = 0

	for eachRow in imgaeArray:
		for eachPix in eachRow:
			if (eachPix[0] == 254  and eachPix[1] == 114 and eachPix[2] == 0):
				orangePx += 1
			elif (eachPix[0] == 254  and eachPix[1] == 205 and eachPix[2] == 165):
				beigePx += 1
			elif (eachPix[0] == 131  and eachPix[1] == 243 and eachPix[2] == 115):
				lightGreenPx += 1
			elif (eachPix[0] == 2  and eachPix[1] == 205 and eachPix[2] == 0):
				greenPx += 1
			elif (eachPix[0] == 1  and eachPix[1] == 130 and eachPix[2] == 0):
				darkGreenPx += 1
			elif (eachPix[0] == 23  and eachPix[1] == 0 and eachPix[2] == 220):
				lightBluePx += 1

def laskePuusto(imgaeArray):
	orangePx = 0
	beigePx = 0
	lightGreenPx = 0
	greenPx = 0
	darkGreenPx = 0
	lightBluePx = 0
	



	for eachRow in imgaeArray:
		for eachPix in eachRow:
			if (eachPix[0] == 254  and eachPix[1] == 114 and eachPix[2] == 0):
				orangePx += 1
			elif (eachPix[0] == 254  and eachPix[1] == 205 and eachPix[2] == 165):
				beigePx += 1
			elif (eachPix[0] == 131  and eachPix[1] == 243 and eachPix[2] == 115):
				lightGreenPx += 1
			elif (eachPix[0] == 2  and eachPix[1] == 205 and eachPix[2] == 0):
				greenPx += 1
			elif (eachPix[0] == 1  and eachPix[1] == 130 and eachPix[2] == 0):
				darkGreenPx += 1
			elif (eachPix[0] == 23  and eachPix[1] == 0 and eachPix[2] == 220):
				lightBluePx += 1



	orange = orangePx / (sqrSize*sqrSize)
	beige = beigePx / (sqrSize*sqrSize)
	lightGreen = lightGreenPx / (sqrSize*sqrSize)
	green = greenPx / (sqrSize*sqrSize)
	darkGreen = darkGreenPx / (sqrSize*sqrSize)
	lightBlue = lightBluePx / (sqrSize*sqrSize)
	
	puustoAla = (orange * 0 +  beige * 1 + lightGreen * 3 + green * 9 + darkGreen * 21 + lightBlue * 42) * 0.0256
	puustoYla = (orange * 0 +  beige * 2 + lightGreen * 8 + green * 20 + darkGreen * 41 + lightBlue * 42) * 0.0256

	print("Koivukuitu:")
	print("orange: " + str(round(orange,2) * 0.0256 * 0))
	print("beige: " + str(round(beige,2) * 0.0256 * 2))
	print("lightGreen: " + str(round(lightGreen,2) * 0.0256 * 4))
	print("green: " + str(round(green,2) * 0.0256 * 9))
	print("darkGreen: " + str(round(darkGreen,2) * 0.0256 * 20))
	print("lightBlue: " + str(round(lightBlue,2) * 0.0256 * 44))
	print(str(puustoAla) + "m^3 (alaraja)")
	print(str(puustoYla) + "m^3 (yläraja)")






iar = np.array(i)

laskePuusto(iar)