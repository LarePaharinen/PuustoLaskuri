from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
import functools as ft
import time


start = time.time()

kohde = "535-402-8-58"
sqrSize = 32
folderPath = "D:\\Vapaa-aika\\Koodaus\\PuustoLaskuri\\images\\" + kohde + "\\"

def laskePuustoMantyTukki(imgaeArray):
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
			if (eachPix[0] == 255 and eachPix[1] == 255 and eachPix[2] == 255):
				continue
			elif (eachPix[0] == 254 and eachPix[1] == 114 and eachPix[2] == 0):
				orangePx += 1
			elif (eachPix[0] == 254 and eachPix[1] == 152 and eachPix[2] == 70):
				brownPx += 1
			elif (eachPix[0] == 254 and eachPix[1] == 205 and eachPix[2] == 165):
				beigePx += 1
			elif (eachPix[0] == 195 and eachPix[1] == 255 and eachPix[2] == 195):
				fadedGreenPx += 1
			elif (eachPix[0] == 131 and eachPix[1] == 243 and eachPix[2] == 115):
				lightGreenPx += 1
			elif (eachPix[0] == 24 and eachPix[1] == 231 and eachPix[2] == 22):
				semiLightGreenPx += 1
			elif (eachPix[0] == 2 and eachPix[1] == 205 and eachPix[2] == 0):
				greenPx += 1
			elif (eachPix[0] == 1 and eachPix[1] == 130 and eachPix[2] == 0):
				darkGreenPx += 1
			elif (eachPix[0] == 23 and eachPix[1] == 0 and eachPix[2] == 220):
				lightBluePx += 1
			elif (eachPix[0] == 40 and eachPix[1] == 31 and eachPix[2] == 149):
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

	puustoAla = (orange * 0 + brown * 1 + beige * 2 + fadedGreen * 3 + lightGreen * 6 +
				 semiLightGreen * 11 + green * 18 + darkGreen * 28 + lightBlue * 42 + darkBlue * 70) * 0.0256
	puustoYla = (orange * 0 + brown * 1 + beige * 2 + fadedGreen * 5 + lightGreen * 10 +
				 semiLightGreen * 18 + green * 27 + darkGreen * 41 + lightBlue * 69 + darkBlue * 70) * 0.0256

	return puustoAla, puustoYla

def laskePuustoKuusiTukki(imgaeArray):
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
			if (eachPix[0] == 255 and eachPix[1] == 255 and eachPix[2] == 255):
				continue
			elif (eachPix[0] == 254 and eachPix[1] == 114 and eachPix[2] == 0):
				orangePx += 1
			elif (eachPix[0] == 254 and eachPix[1] == 152 and eachPix[2] == 70):
				brownPx += 1
			elif (eachPix[0] == 254 and eachPix[1] == 205 and eachPix[2] == 165):
				beigePx += 1
			elif (eachPix[0] == 195 and eachPix[1] == 255 and eachPix[2] == 195):
				fadedGreenPx += 1
			elif (eachPix[0] == 131 and eachPix[1] == 243 and eachPix[2] == 115):
				lightGreenPx += 1
			elif (eachPix[0] == 24 and eachPix[1] == 231 and eachPix[2] == 22):
				semiLightGreenPx += 1
			elif (eachPix[0] == 2 and eachPix[1] == 205 and eachPix[2] == 0):
				greenPx += 1
			elif (eachPix[0] == 1 and eachPix[1] == 130 and eachPix[2] == 0):
				darkGreenPx += 1
			elif (eachPix[0] == 23 and eachPix[1] == 0 and eachPix[2] == 220):
				lightBluePx += 1
			elif (eachPix[0] == 40 and eachPix[1] == 31 and eachPix[2] == 149):
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

	puustoAla = (orange * 0 + brown * 1 + beige * 2 + fadedGreen * 3 + lightGreen * 4 +
				 semiLightGreen * 5 + green * 9 + darkGreen * 20 + lightBlue * 44 + darkBlue * 107) * 0.0256
	puustoYla = (orange * 0 + brown * 1 + beige * 2 + fadedGreen * 3 + lightGreen * 4 +
				 semiLightGreen * 8 + green * 19 + darkGreen * 43 + lightBlue * 106 + darkBlue * 107) * 0.0256

	return puustoAla, puustoYla
	
def laskePuustoKoivuTukki(imgaeArray):
	orangePx = 0
	beigePx = 0
	lightGreenPx = 0
	greenPx = 0
	darkGreenPx = 0
	lightBluePx = 0

	for eachRow in imgaeArray:
		for eachPix in eachRow:
			if (eachPix[0] == 255 and eachPix[1] == 255 and eachPix[2] == 255):
				continue
			elif (eachPix[0] == 254  and eachPix[1] == 114 and eachPix[2] == 0):
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
	
	puustoAla = (orange * 0 +  beige * 1 + lightGreen * 2 + green * 3 + darkGreen * 4 + lightBlue * 9) * 0.0256
	puustoYla = (orange * 0 +  beige * 1 + lightGreen * 2 + green * 3 + darkGreen * 8 + lightBlue * 9) * 0.0256

	return puustoAla, puustoYla

def laskePuustoMantyKuitu(imgaeArray):
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
			if (eachPix[0] == 255 and eachPix[1] == 255 and eachPix[2] == 255):
				continue
			elif (eachPix[0] == 254  and eachPix[1] == 114 and eachPix[2] == 0):
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

	puustoAla = (orange * 0 + brown * 1 + beige * 6 + fadedGreen * 14 + lightGreen * 24 + semiLightGreen * 35 + green * 47 + darkGreen * 59 + lightBlue * 72 + darkBlue * 93) * 0.0256
	puustoYla = (orange * 0 + brown * 5 + beige * 13 + fadedGreen * 23 + lightGreen * 34 + semiLightGreen * 46 + green * 58 + darkGreen * 71 + lightBlue * 92 + darkBlue * 93) * 0.0256

	return puustoAla, puustoYla

def laskePuustoKuusiKuitu(imgaeArray):
	orangePx = 0
	beigePx = 0
	lightGreenPx = 0
	greenPx = 0
	darkGreenPx = 0
	lightBluePx = 0

	for eachRow in imgaeArray:
		for eachPix in eachRow:
			if (eachPix[0] == 255 and eachPix[1] == 255 and eachPix[2] == 255):
				continue
			elif (eachPix[0] == 254  and eachPix[1] == 114 and eachPix[2] == 0):
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
	
	puustoAla = (orange * 0 +  beige * 1 + lightGreen * 3 + green * 9 + darkGreen * 27 + lightBlue * 62) * 0.0256
	puustoYla = (orange * 0 +  beige * 2 + lightGreen * 8 + green * 26 + darkGreen * 61 + lightBlue * 62) * 0.0256

	return puustoAla, puustoYla

def laskePuustoKoivuKuitu(imgaeArray):
	orangePx = 0
	beigePx = 0
	lightGreenPx = 0
	greenPx = 0
	darkGreenPx = 0
	lightBluePx = 0

	for eachRow in imgaeArray:
		for eachPix in eachRow:
			if (eachPix[0] == 255 and eachPix[1] == 255 and eachPix[2] == 255):
				continue
			elif (eachPix[0] == 254  and eachPix[1] == 114 and eachPix[2] == 0):
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

	return puustoAla, puustoYla

def laskePuustoYht(imgaeArray):
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
			if (eachPix[0] == 255 and eachPix[1] == 255 and eachPix[2] == 255):
				continue
			elif (eachPix[0] == 254  and eachPix[1] == 114 and eachPix[2] == 0):
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

	return puustoAla, puustoYla


iMäntyTukki = Image.open(folderPath + "mäntyTukki.png")
iArMäntyTukki = np.array(iMäntyTukki)
mäntyTukki = laskePuustoMantyTukki(iArMäntyTukki)
print("MäT valmis(1/7)")

iKuusiTukki = Image.open(folderPath + "kuusiTukki.png")
iArKuusiTukki = np.array(iKuusiTukki)
kuusiTukki = laskePuustoKuusiTukki(iArKuusiTukki)
print("KuT valmis(2/7)")

iKoivuTukki = Image.open(folderPath + "koivuTukki.png")
iArKoivuTukki = np.array(iKoivuTukki)
koivuTukki = laskePuustoKoivuTukki(iArKoivuTukki)
print("KoT valmis(3/7)")

iMäntyKuitu = Image.open(folderPath + "mäntyKuitu.png")
iArMäntyKuitu = np.array(iMäntyKuitu)
mäntyKuitu = laskePuustoMantyKuitu(iArMäntyKuitu)
print("MäK valmis(4/7)")

iKuusiKuitu = Image.open(folderPath + "kuusiKuitu.png")
iArKuusiKuitu = np.array(iKuusiKuitu)
kuusiKuitu = laskePuustoKuusiKuitu(iArKuusiKuitu)
print("KuK valmis(5/7)")

iKoivuKuitu = Image.open(folderPath + "koivuKuitu.png")
iArKoivuKuitu = np.array(iKoivuKuitu)
koivuKuitu = laskePuustoKoivuKuitu(iArKoivuKuitu)
print("KoK valmis(6/7)")

iPuustoYht = Image.open(folderPath + "puustoYht.png")
iArPuustoYht = np.array(iPuustoYht)
puustoYht = laskePuustoYht(iArPuustoYht)
print("Kaikki valmiina! (7/7)")

filename = kohde + ".csv"

f = open(filename, "w")

headers = " , ala, ylä\n"

f.write(headers)
f.write("MäT," + str(round(mäntyTukki[0],3)) + ", " + str(round(mäntyTukki[1],3)) + "\n")
f.write("KuT," + str(round(kuusiTukki[0],3)) + ", " + str(round(kuusiTukki[1],3)) + "\n")
f.write("KoT," + str(round(koivuTukki[0],3)) + ", " + str(round(koivuTukki[1],3)) + "\n")
f.write("MäK," + str(round(mäntyKuitu[0],3)) + ", " + str(round(mäntyKuitu[1],3)) + "\n")
f.write("KuK," + str(round(kuusiKuitu[0],3)) + ", " + str(round(kuusiKuitu[1],3)) + "\n")
f.write("KoK," + str(round(koivuKuitu[0],3)) + ", " + str(round(koivuKuitu[1],3)) + "\n")
f.write("PuustoYht," + str(round(puustoYht[0],3)) + ", " + str(round(puustoYht[1],3)) + "\n")

f.close()

end = time.time()

print(end - start)


