from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
import functools as ft


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
	sqrSize = 32




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

	puusto = orange * 2 + brown * 16.5 + beige * 41.5 + fadedGreen * 66 + lightGreen * 89 + semiLightGreen * 114.5 + green * 144.5 + darkGreen * 180 + lightBlue * 232 + darkBlue * 270

	print("orange: " + str(round(orange,2)))
	print("brown: " + str(round(brown,2)))
	print("beige: " + str(round(beige,2)))
	print("fadedGreen: " + str(round(fadedGreen,2)))
	print("lightGreen: " + str(round(lightGreen,2)))
	print("semiLightGreen: " + str(round(semiLightGreen,2)))
	print("green: " + str(round(green,2)))
	print("darkGreen: " + str(round(darkGreen,2)))
	print("lightBlue: " + str(round(lightBlue,2)))
	print("darkBlue: " + str(round(darkBlue,2)))
	print(str(puusto) + "m^3")





i = Image.open("images/ala1.png")
iar = np.array(i)

laskePuusto(iar)


'''def threshold(imgaeArray):
	balanceAr = []
	newAr = imgaeArray

	for eachRow in imgaeArray:
		for eachPix in eachRow:
			avgNum = ft.reduce(lambda x, y: x + y, eachPix[:3])/len(eachPix[:3])
			balanceAr.append(avgNum)

	balance = ft.reduce(lambda x, y: x + y, balanceAr)/len(balanceAr)


	for eachRow in newAr:
		for eachPix in eachRow:
			if ft.reduce(lambda x, y: x + y, eachPix[:3])/len(eachPix[:3]) > balance:
				eachPix[0] = 255
				eachPix[1] = 255
				eachPix[2] = 255
				eachPix[3] = 255

			else:
				eachPix[0] = 0
				eachPix[1] = 0
				eachPix[2] = 0
				eachPix[3] = 255

	return newAr

i = Image.open("images/numbers/0.1.png")
iar = np.array(i)

i2 = Image.open("images/numbers/y0.4.png")
iar2 = np.array(i2)

i3 = Image.open("images/numbers/y0.5.png")
iar3 = np.array(i3)

i4 = Image.open("images/sentdex.png")
iar4 = np.array(i4)

threshold(iar3)
threshold(iar2)
#threshold(iar4)

fig = plt.figure()

ax1 = plt.subplot2grid((8,6),(0,0),rowspan=4,colspan = 3)
ax2 = plt.subplot2grid((8,6),(4,0),rowspan=4,colspan = 3)
ax3 = plt.subplot2grid((8,6),(0,3),rowspan=4,colspan = 3)
ax4 = plt.subplot2grid((8,6),(4,3),rowspan=4,colspan = 3)

ax1.imshow(iar)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)

plt.show()'''