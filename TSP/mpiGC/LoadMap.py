from BuildMap import buildMap
import numpy as np
from os import path

def loadMap(cityCount):
	fileName = f"spp{cityCount}.bin"
	print("We will open file:", fileName)
	if(path.exists(fileName)):
		print ("File exists")
		cityMap = np.fromfile (fileName, dtype=np.int, count = -1)
		cityMap = np.reshape(cityMap, (cityCount, cityCount))
		#print(cityMap)
		return cityMap
	else:
		print("File does not exist.")
		print("Building map.")
		buildMap(cityCount, fileName)
		loadMap(cityCount)
        #loadMap(cityCount, cityMap)