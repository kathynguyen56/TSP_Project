import numpy as np
import random

def buildMap(cityCount, fileName):
    print("We are going to build a map for", cityCount, "cities.")
    rows, cols = (cityCount, cityCount)
    cityMap = [[0 for i in range(cols)] for j in range(rows)]

    for rowIndex in range(rows):
        for columnIndex in range(cols):
            cityMap[rowIndex][columnIndex] = random.randint(10,99)

    print(cityMap)
    np.array(cityMap).tofile(fileName)
