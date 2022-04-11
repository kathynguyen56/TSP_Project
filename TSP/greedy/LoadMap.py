#LoadMap
from BuildMap import buildMap
import numpy as np
import os.path
from os import path

def loadMap(cityCount, cityMap):
    loadMapGreeting = f"Hello, we will have {cityCount} cities"
    print(loadMapGreeting)
    fileName = f"spp{cityCount}.bin"
    print("We want to open file:", fileName)
    if(path.exists(fileName)):
        print ("File exists")
        cityMap = np.fromfile(fileName,  dtype=np.int, count = -1)
        cityMap = np.reshape(cityMap,(cityCount,cityCount))
        print(cityMap)
        return cityMap
    else:
        print("File does not exist")
        print("Building map.")
        buildMap(cityCount,fileName)
        loadMap(cityCount, cityMap)
