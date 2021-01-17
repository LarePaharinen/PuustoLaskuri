from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
import functools as ft

sqrSize = 8
i = Image.open("C:\\Users\\lauri\\Desktop\\puustoYht.png")

def laskePuusto(imgaeArray):
	orangePx = 0
	brownPx = 0
	beigePx = 0
	fadedGreenPx = 0
	lightGreenPx = 0
	semiLightGreenPx = 0
	greenPx = 0
	darkGreenPx = 0
	lightBluePx = 0
	darkBluePx = 0




	for eachRow in imgaeArray:
		for eachPix in eachRow:
			if (eachPix[0] == 254  and eachPix[1] == 114 and eachPix[2] == 0):
				orangePx += 1
			elif (eachPix[0] == 254  and eachPix[1] == 152 and eachPix[2] == 70):
				brownPx += 1
			elif (eachPix[0] == 254  and eachPix[1] == 205 and eachPix[2] == 165):
				beigePx += 1
			elif (eachPix[0] == 195  and eachPix[1] == 255 and eachPix[2] == 195):
				fadedGreenPx += 1
			elif (eachPix[0] == 131  and eachPix[1] == 243 and eachPix[2] == 115):
				lightGreenPx += 1
			elif (eachPix[0] == 24  and eachPix[1] == 231 and eachPix[2] == 22):
				semiLightGreenPx += 1
			elif (eachPix[0] == 2  and eachPix[1] == 205 and eachPix[2] == 0):
				greenPx += 1
			elif (eachPix[0] == 1  and eachPix[1] == 130 and eachPix[2] == 0):
				darkGreenPx += 1
			elif (eachPix[0] == 23  and eachPix[1] == 0 and eachPix[2] == 220):
				lightBluePx += 1
			elif (eachPix[0] == 40  and eachPix[1] == 31 and eachPix[2] == 149):
				darkBluePx += 1



	orange = orangePx / (sqrSize*sqrSize)
	brown = brownPx / (sqrSize*sqrSize)
	beige = beigePx / (sqrSize*sqrSize)
	fadedGreen = fadedGreenPx / (sqrSize*sqrSize)
	lightGreen = lightGreenPx / (sqrSize*sqrSize)
	semiLightGreen = semiLightGreenPx / (sqrSize*sqrSize)
	green = greenPx / (sqrSize*sqrSize)
	darkGreen = darkGreenPx / (sqrSize*sqrSize)
	lightBlue = lightBluePx / (sqrSize*sqrSize)
	darkBlue = darkBluePx / (sqrSize*sqrSize)

	puustoAla = (orange * 0 + brown * 5 + beige * 29 + fadedGreen * 55 + lightGreen * 78 + semiLightGreen * 101 + green * 129 + darkGreen * 161 + lightBlue * 201 + darkBlue * 264) * 0.0256
	puustoYla = (orange * 4 + brown * 28 + beige * 56 + fadedGreen * 77 + lightGreen * 100 + semiLightGreen * 128 + green * 160 + darkGreen * 200 + lightBlue * 263 + darkBlue * 264) * 0.0256

	print("Puusto Yht:")
	print("orange: " + str(round(orange,2) * 0.0256 * 0))
	print("brown: " + str(round(brown,2) * 0.0256 * 1))
	print("beige: " + str(round(beige,2) * 0.0256 * 2))
	print("fadedGreen: " + str(round(fadedGreen,2) * 0.0256 * 3))
	print("lightGreen: " + str(round(lightGreen,2) * 0.0256 * 4))
	print("semiLightGreen: " + str(round(semiLightGreen,2) * 0.0256 * 5))
	print("green: " + str(round(green,2) * 0.0256 * 9))
	print("darkGreen: " + str(round(darkGreen,2) * 0.0256 * 20))
	print("lightBlue: " + str(round(lightBlue,2) * 0.0256 * 44))
	print("darkBlue: " + str(round(darkBlue,2) * 0.0256 * 107))
	print("Pinta-ala: " + str(orange+brown+beige+fadedGreen+lightGreen+semiLightGreen+green+darkGreen+lightBlue+darkBlue))
	print(str(puustoAla) + "m^3 (alaraja)")
	print(str(puustoYla) + "m^3 (yläraja)")






iar = np.array(i)

laskePuusto(iar)