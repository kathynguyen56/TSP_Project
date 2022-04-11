from GetPath import getRandomPath
from GetPathDistance import getPathDistance
import numpy as np
import random
import time

def greedy(path,cityMap):
    #print("\n\nStart of Greedy Algorithm")

    startTime = time.time()
    failToImprove = 0
    noPath = [0 for i in range(len(path))]
    tempPath = noPath.copy()


    #getRandomPath(tempPath)
    #shortestDistance = getPathDistance(tempPath,cityMap)
    #print("Random start, shortest distance:",shortestDistance)
    citiesToVisitStart = [i for i in range(len(path))]
    #for index in range(len(path)):
            #citiesToVisitStart[index] = index
    citiesToVisit = citiesToVisitStart.copy()
    citiesToVisit.remove(tempPath[0])

    getGreedyPath(tempPath,citiesToVisit,cityMap)

    tempDistance =  getPathDistance(tempPath,cityMap)

    #print("Distance:", tempDistance),
    #print(tempPath)

    shortestDistance = tempDistance
    path = tempPath.copy()
    tempDistance = 0
    limitOnTimesToFailToImprove = 1000
    startingCity = 1

    while(startingCity < len(path)):
        citiesToVisit = citiesToVisitStart.copy()



        tempPath = noPath.copy()
        #print("Cities to visit at start",citiesToVisit)

        tempPath[0] = startingCity
        citiesToVisit.remove(startingCity)

        startingCity = startingCity + 1

        #print("Place to start:", tempPath[0])
        #print("Temp path",tempPath)
        #print("Cities to visit after picking random city",citiesToVisit)

        getGreedyPath(tempPath,citiesToVisit,cityMap)

        tempDistance =  getPathDistance(tempPath,cityMap)

        #print("Distance:", tempDistance),
        #print(tempPath)

        if(tempDistance < shortestDistance):
            path = tempPath.copy()
            shortestDistance = tempDistance
            #print("Shortest distance:",shortestDistance)
        else:
            failToImprove = failToImprove + 1
            #print("Failed to improve.")

    stopTime = time.time()
    print("Greedy Path:", path)
    distance = getPathDistance(path,cityMap)
    print("Greedy Distance:", distance)
    print("Greedy Time:", (stopTime - startTime))

def pickRandomCity(citiesToVisit):
    nextCity = random.choice(citiesToVisit)
    citiesToVisit.remove(nextCity)
    return nextCity

def getGreedyPath(tempPath,citiesToVisit,cityMap):
    #print("Working Greedy Algorithm (Meat)")
    nearestNeighborMax = np.amax(cityMap)
    for index in range((len(tempPath)-1)):
        #print("Where I am:", tempPath[index])
        #print("Cities To Visit:", citiesToVisit)
        #print(cityMap)
        nearestNeighbor = nearestNeighborMax
        for checkIndex in range(len(citiesToVisit)):
            nextDistance = cityMap[tempPath[index]][citiesToVisit[checkIndex]]
            #print("Next Distance", nextDistance)
            if(nextDistance <= nearestNeighbor):
                nearestNeighbor = nextDistance
                nextCity = citiesToVisit[checkIndex]
        #load the winner from those cities to Visit
        tempPath[index+1] = nextCity
        #print("Updated temp path:", tempPath)
        #print("We go to:", nextCity)
        citiesToVisit.remove(nextCity)
