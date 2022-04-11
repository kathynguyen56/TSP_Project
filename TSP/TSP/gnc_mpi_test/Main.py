from array import array
from GetPath import getRandomPath
from GetPathDistance import getPathDistance
from Greedy import greedy
from Greeting import displayGreeting
from LoadMap import loadMap
#https://www.obeythetestinggoat.com/

cityCount = 10
rows, cols = (cityCount, cityCount)
cityMap = [[0 for i in range(cols)] for j in range(rows)]
path = [0 for i in range(cols)]

displayGreeting()
cityMap = loadMap(cityCount, cityMap)
greedy(path,cityMap)