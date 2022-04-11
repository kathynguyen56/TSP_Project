import numpy as np
import random

def buildMap(cityCount, fileName):
	print("We are going to build a map for ", cityCount, " cities.")
	cityMap = [[0 for i in range(cityCount)] for j in range(cityCount)]
	
	for rowIndex in range(cityCount):
		for columnIndex in range(cityCount):
			cityMap[rowIndex][columnIndex] = random.randint(10,99)
	
	#print(cityMap)
	np.array(cityMap).tofile(fileName)