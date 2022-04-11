import random
from array import array
#from GuessAndCheck import guessAndCheck
from LoadMap import loadMap
import numpy as np
import bisect

print("Welcome to the Shortest Path program.")

cityCount = 6
print("Our city count is", cityCount)
path = [0 for i in range(cityCount)]

cityMap = loadMap(cityCount)
print(cityMap)
print("If I didn't print out a city matrix, run me again!")

startingCity = 0
#startingCity = random.randint(0, cityCount)
print(startingCity)

#search array pass in startingCity
#find min value based on row
#find location of that min
# add location to path
# find next lowest value
# check if lowest value location is not already in the path

def minRow(cityMap, cityCount):
    for i in range(cityCount):
        min = cityMap[i][0]

        for j in range(1,cityCount,1):
            if (cityMap[i][j] < min):
                min = cityMap[i][j]
        print(min)

print(minRow(cityMap, cityCount))

print("new")
startingCity = cityMap[0]
print('Starting city: ' + str(cityMap[0]))

#Begin at the first city
nextCity = startingCity

#Find the min val of cityMap[0]
print(str(cityMap[0].min()))

#set the next city with smallest dist
min = np.min(cityMap[0])

print(str(min))

#Find the index of the min val
closestCity = np.where(cityMap[0] == min)
print('first closest city' + str(closestCity))

path = int(closestCity[0])
print (path)


nextCity = closestCity
print(str(cityMap[nextCity].min()))
min = np.min(cityMap[nextCity])
 if 
    closestCity = np.where(cityMap[nextCity] == min)
    print('next closest city'+ str(closestCity))


print('test case')
startingCity = 0
print('City: ' + str(cityMap[0]))



for j in range(0, len(cityMap[startingCity])):

       # print('City: ' + str(j))
        print('j: ' + str(j))
        print('nextCityDistance: ' + str(cityMap[1][j]))
        if int(cityMap[1][j]) < int(cityMap[1][j+1]):
            print('Index at City[ ' + str(j) + '] is smaller')
            temp = cityMap[1][j]
            print(temp)









