from GetPath import getRandomPath
from GetPathDistance import getPathDistance
import numpy as np
import random
import time
from mpi4py import MPI

def greedy(path,cityMapStart):

    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()
    #print("\n\nStart of Greedy Algorithm")

    if rank == 0:
        print("hello I am rank" ,rank)


    timeLimit = 300
    startTime = time.time()
    failToImprove = 0
    #noPath = [0 for i in range(len(path))]
    #tempPath = noPath.copy()
    noPath = []
    #tempPath = noPath.copy()

    #getRandomPath(tempPath)
    #shortestDistance = getPathDistance(tempPath,cityMap)
    #print("Random start, shortest distance:",shortestDistance)
    citiesToVisitStart = [i for i in range(len(path))]
    #print(f' cities to visit {citiesToVisitStart}')
    #for index in range(len(path)):
            #citiesToVisitStart[index] = index
    #citiesToVisit = citiesToVisitStart.copy()
    cityMap = cityMapStart.copy()
    startingCity = 0 + rank
    begin = startingCity






    for startingCity in range (0, len(path)):
        if (startingCity % size == rank and begin % size == rank):
           # print("     Rank:", rank, "   StartingCity:", startingCity)
            begin = startingCity - 1

            citiesToVisit = citiesToVisitStart.copy()
            tempPath = noPath.copy()
            tempPath.append(startingCity)
            citiesToVisit.remove(startingCity)
##            getGreedyPath(tempPath, citiesToVisit, cityMap)
#            print("Rank:", rank, "Starting findMin for city", startingCity)
            findMin(tempPath, citiesToVisit, cityMap, begin, path)
#            print("Rank:", rank, "Finishing findMin for city", startingCity)


            tempDistance =  getPathDistance(tempPath,cityMap)
#           print("Rank:", rank, "   Starting city:", startingCity, "Path:", tempPath, "   Distance:", tempDistance)

            if (startingCity < size):
                path = tempPath
                distance = tempDistance

            elif (tempDistance < distance):
                path = tempPath
                distance = tempDistance
                print("New shortest distance:", distance)

        stopTime = time.time()
        elapsedTime = stopTime - startTime
        if (elapsedTime >= timeLimit - 2):
            #print("    TIME:", elapsedTime)
            break


    #print(rank, "is at the barrier")
    comm.barrier()
    #print(rank, "has crossed the barrier")

    if (rank == 0):
        stopTime = time.time()
        print("Shortest distance:", distance, "   Time:", stopTime - startTime)

    clusterShortestGreedy = comm.allreduce(distance, MPI.MIN)

    comm.barrier()

    if (distance == clusterShortestGreedy):
        comm.send(path, dest=0)

    if (rank == 0):
        shortestPath = comm.recv(source=MPI.ANY_SOURCE)

        print("Greedy Path:", shortestPath)
        print("Greedy Distance:", clusterShortestGreedy)
        print("Greedy Time:", (stopTime - startTime))






    """

    nextCityIndex = 0
    begin =startingCity;

    #print(f' temppath[0] {tempPath[0]}')
    tempPath.append(startingCity)
    citiesToVisit.remove(startingCity)
    #print(f' cities to visit {citiesToVisit}')


#    print(f' temp path {tempPath}')
    #getGreedyPath(tempPath,citiesToVisit,cityMap)
    #getGreedyMin(tempPath, citiesToVisit, cityMap, startingCity)
    #getGreedyMin2(tempPath, citiesToVisit, cityMap, begin, nextCityIndex)
    findMin(tempPath, citiesToVisit, cityMap, begin,path)
#    print(f' temp path after getGreedyMin2 {tempPath}')

    tempDistance = getPathDistance(tempPath,cityMap)

#    print("Distance:", tempDistance),
#    print(tempPath)

    shortestDistance = tempDistance
    path = tempPath.copy()
    tempDistance = 0
    limitOnTimesToFailToImprove = 1000

    while_counter = 0
    while(startingCity < len(path)):
        citiesToVisit = citiesToVisitStart.copy()
        cityMap = cityMapStart.copy()
        #citiesToVisit = citiesToVisitStart
#        print(f' while counter {while_counter}')
        tempPath = noPath.copy()
        #print("Cities to visit at start",citiesToVisit)

        #tempPath[0] = startingCity
        tempPath.append(startingCity)
        citiesToVisit.remove(startingCity)

        startingCity = startingCity + 1
        begin = startingCity - 1
#        print(f' begin is {begin}')

#        print("Place to start:", tempPath[0])
        #print("Temp path",tempPath)
        #print("Cities to visit after picking random city",citiesToVisit)

        #getGreedyPath(tempPath,citiesToVisit,cityMap)
        #getGreedyMin(tempPath,citiesToVisit, cityMap, startingCity)
        #getGreedyMin2(tempPath, citiesToVisit, cityMap, begin)
        findMin(tempPath, citiesToVisit, cityMap, begin, path)
        tempDistance = getPathDistance(tempPath,cityMap)

#        print("Distance:", tempDistance),
        #print(tempPath)

        if(tempDistance < shortestDistance):
            path = tempPath.copy()
            shortestDistance = tempDistance
#            print("Shortest distance:",shortestDistance)
        else:
            failToImprove = failToImprove + 1
#            print("Failed to improve.")
    while_counter += 1
#    print(f' while_counter after {while_counter}')
    stopTime = time.time()
    print("Greedy Path:", path)
    distance = getPathDistance(path,cityMapStart)
    print("Greedy Distance:", distance)
    print("Greedy Time:", (stopTime - startTime))


    """

def findMin(tempPath, citiesToVisit, cityMap, begin, path):
#    print(cityMap)
    minArray = np.argmin(cityMap, axis=1)
#    print(f' This is the min array {minArray}')
    #print(f' nextCityIndex {nextCityIndex}')
#    print(f' line 94 cities to visit {citiesToVisit}')
    #for index in range(len(path)+2):
    while (len(tempPath) != len(path)):
        minArray = np.argmin(cityMap, axis=1)
#        print(f' This is the min array {minArray}')
#        print(f' minarray {minArray[begin]}')
        nextCityIndex = minArray[begin]
    #while len(citiesToVisit) >= 1:
        if nextCityIndex in citiesToVisit:
#                print(f" This city {nextCityIndex} has not been visited")
                citiesToVisit.remove(nextCityIndex)
               #print(f' this is the IDEX {index}')
                #tempPath[index] = nextCityIndex
                tempPath.append(nextCityIndex)
#                print(f' current tempPath {tempPath}')
#                print(f' line 99 cities to visit {citiesToVisit}')
                begin = nextCityIndex
                #findMin(tempPath, citiesToVisit, cityMap, begin)
                # startingCity = nextCityIndex
                # cityMap = cityMapCopy

        else:
            cityMap[begin, nextCityIndex] = 100000
#            print(cityMap)
#            print(f"This city {nextCityIndex} been visited")
            #findMin(tempPath, citiesToVisit, cityMap, begin)


def getGreedyMin2(tempPath, citiesToVisit, cityMap, begin, nextCityIndex):
    minArray = np.argmin(cityMap, axis=1)
#    print(f' This is the min array {minArray}')
    cityMapCopy = cityMap.copy()
    for index in range((len(tempPath) - 1)):
#        print("Where I am:", tempPath[index])
#        print(f' this is the index {index}')
#        print("Cities To Visit:", citiesToVisit)
#        print(cityMap)
        """print(f' minarray {minArray[begin]}')
        nextCityIndex = minArray[begin]
        print(f' nextCityIndex {nextCityIndex}')
        print(f' line 94 cities to visit {citiesToVisit}')"""
        for checkIndex in range(len(citiesToVisit)):
            findMin(tempPath, citiesToVisit, cityMap, begin)



def getGreedyMin(tempPath, citiesToVisit, cityMap, startingCity):
    minArray = np.argmin(cityMap, axis=1)
#    print(f' minarray {minArray[startingCity]}')
    nextCityIndex = minArray[startingCity]
#    print(f' startingCity {startingCity}')
#    print(f' line 94 cities to visit {citiesToVisit}')
    while (len(citiesToVisit) != 0):
        if nextCityIndex in citiesToVisit:
#            print(f" This city {nextCityIndex} has not been visited")
            citiesToVisit.remove(nextCityIndex)
            tempPath[startingCity + 1] = nextCityIndex
#            print(f' line 99 cities to visit {citiesToVisit}')
            startingCity +=1
            #startingCity = nextCityIndex
        else:
            cityMap[startingCity, nextCityIndex] = 100000
#            print(cityMap)
#            print(f"This city {nextCityIndex} been visited")
            getGreedyMin(tempPath, citiesToVisit, cityMap, startingCity)



    """for index in range((len(tempPath) - 1)):
        print("Where I am:", tempPath[index])
        print("Cities To Visit:", citiesToVisit)
        print(cityMap)
        nearestNeighborMax = np.amax(cityMap)
        print(f' nearest neighbor max is {nearestNeighborMax}')
        nearestNeighborMin = np.amin(cityMap[index])
        nearestNeighbor = nearestNeighborMin
        print(f'citymap[index is {cityMap[index]}')
        for checkIndex in range(len(citiesToVisit)):
            if (np.where(cityMap[index] == nearestNeighborMin) not in citiesToVisit) :
                nextCity = np.where(cityMap[index] == nearestNeighborMin)
                print(f'nearest neighbor is {nearestNeighbor}')
                print(f' next city is {nextCity}')
                nextCityIndex = int(nextCity[0])
                cityMap[tempPath[index]][citiesToVisit[checkIndex]] = nearestNeighborMax
                nearestNeighborMin = np.amin(cityMap[index])
                print(cityMap)
                print(f' new nearest Neighbor {nearestNeighborMin}')
                print(f' nextCityIndex is {nextCityIndex}')
                citiesToVisit.remove(nextCityIndex) """

         #nearestNeighbor = np.amin(cityMap[tempPath[index]][citiesToVisit[checkIndex]])
            #print(cityMap[tempPath[index]][citiesToVisit[checkIndex]])
            #print(f'new nearest neighbor{nearestNeighbor}')
            #nextDistance = cityMap[tempPath[index]][citiesToVisit[checkIndex]]
            #print("Next Distance", nextDistance)
            #if (nearestNeighbor == nextDistance):
                #nearestNeighbor = nextDistance
                #nextCity = citiesToVisit[checkIndex]
                #print(f'nearestNeighbor {nearestNeighbor}')
                #print(f'nextcity is {nextCity}')
                #break
        # load the winner from those cities to Visit
        #tempPath[index + 1] = nextCity
        #print("Updated temp path:", tempPath)
        #print("We go to:", nextCity)
        #citiesToVisit.remove(nextCity)



def getGreedyPath(tempPath,citiesToVisit,cityMap):
    #print("Working Greedy Algorithm (Meat)")
    nearestNeighborMax = np.amax(cityMap)
    for index in range((len(tempPath)-1)):
#        print("Where I am:", tempPath[index])
#        print("Cities To Visit:", citiesToVisit)
#        print(cityMap)
        nearestNeighbor = nearestNeighborMax
#        print(f'nearest neighbor is {nearestNeighbor}')
        for checkIndex in range(len(citiesToVisit)):
            nextDistance = cityMap[tempPath[index]][citiesToVisit[checkIndex]]
#            print("Next Distance", nextDistance)
            if(nextDistance <= nearestNeighbor):
                nearestNeighbor = nextDistance
                nextCity = citiesToVisit[checkIndex]
#                print(f'nextcity is {nextCity}')
        #load the winner from those cities to Visit
        tempPath[index+1] = nextCity
        #print("Updated temp path:", tempPath)
        #print("We go to:", nextCity)
        citiesToVisit.remove(nextCity)
