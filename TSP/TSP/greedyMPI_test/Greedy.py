from GetPath import getRandomPath
from GetPathDistance import getPathDistance
import numpy as np
import random
import time
from mpi4py import MPI


def greedy(path,cityMap):

    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()
    
    timeLimit = 300
    
    noPath = [0 for i in range(len(path))]
    tempPath = noPath.copy()
    
    citiesToVisitStart = [i for i in range(len(path))]
    
    citiesToVisit = citiesToVisitStart.copy()
    
    startingCity = 0 + rank
    
    startTime = time.time()
    
    for startingCity in range (0, len(path)):
        if (startingCity % size == rank):
            
            citiesToVisit = citiesToVisitStart.copy()
            tempPath = noPath.copy()
            tempPath[0] = startingCity
            citiesToVisit.remove(startingCity)
            getGreedyPath(tempPath, citiesToVisit, cityMap)
            
            
            tempDistance =  getPathDistance(tempPath,cityMap)
#            print("Starting city:", startingCity, "   Distance:", tempDistance)
            
            if (startingCity < size):
                path = tempPath
                distance = tempDistance
            
            elif (tempDistance < distance):
                path = tempPath
                distance = tempDistance
 #               print("New shortest distance:", distance)
                
        stopTime = time.time()
        elapsedTime = stopTime - startTime
        if (elapsedTime >= timeLimit - 2):
            #print("    TIME:", elapsedTime)
            break

    
    
    comm.barrier()
    
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


def getGreedyPath(tempPath,citiesToVisit,cityMap):
    nearestNeighborMax = np.amax(cityMap)
    for index in range((len(tempPath)-1)):
        nearestNeighbor = nearestNeighborMax
        
        for checkIndex in range(len(citiesToVisit)):
            nextDistance = cityMap[tempPath[index]][citiesToVisit[checkIndex]]
            
            if(nextDistance <= nearestNeighbor):
                nearestNeighbor = nextDistance
                nextCity = citiesToVisit[checkIndex]
                
        tempPath[index+1] = nextCity
        citiesToVisit.remove(nextCity)

        
        
        
        
