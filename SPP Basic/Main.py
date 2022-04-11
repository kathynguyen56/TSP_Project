from array import array
from GuessAndCheck import guessAndCheck
from LoadMap import loadMap

print("Welcome to the Shortest Path program.")

cityCount = 5
print("Our city count is", cityCount)
path = [0 for i in range(cityCount)]

cityMap = loadMap(cityCount)
print(cityMap)
print("If I didn't print out a city matrix, run me again!")
