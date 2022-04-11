from array import array
from GetPath import getRandomPath
from GetPathDistance import getPathDistance
from Greedy import greedy
from Greeting import displayGreeting
from LoadMap import loadMap
#https://www.obeythetestinggoat.com/

cityCount = 600
fileName = f"spp{cityCount}.bin"
rows, cols = (cityCount, cityCount)
cityMap = [[0 for i in range(cols)] for j in range(rows)]
path = [0 for i in range(cols)]

cityMap = loadMap(cityCount, cityMap, fileName)
greedy(path,cityMap)
