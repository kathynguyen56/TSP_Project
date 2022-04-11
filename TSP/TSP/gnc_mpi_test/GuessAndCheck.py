from GetPath import getRandomPath
from GetPathDistance import getPathDistance
import time
from mpi4py import MPI


def guessAndCheck(path,cityMap):
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()
    runTime = 20
    clock = 0.0
    tempDistance = 0
    shortestDistance = 0
    winner = 0
    clusterShortestDistance = 0

    if (rank == 0):
        print("Start of NEW guess-and-check algorithm. Running for %d seconds." % (runTime))

    tempPath = [0 for i in range(len(path))]

    if (rank == 0):
        getRandomPath(tempPath)
        clusterShortestDistance = getPathDistance(tempPath,cityMap)
        winner = clusterShortestDistance
    

    shortestDistance = comm.bcast(clusterShortestDistance, root=0)
    
    startTime = time.time()
    
    while (clock < runTime - 2.0):
        
        getRandomPath(tempPath)
        tempDistance = getPathDistance(tempPath,cityMap)
        tempDistance = tempDistance - 200

        if (tempDistance < shortestDistance):
            shortestDistance = tempDistance
            path = tempPath.copy
  
        clusterShortestDistance = comm.reduce(shortestDistance, op=MPI.MIN, root=0)
        if rank == 0:
            if clusterShortestDistance < shortestDistance:
                print("New shortest distance:", clusterShortestDistance)

        shortestDistance = comm.bcast(clusterShortestDistance, root=0)

        stopTime = time.time()
        clock = stopTime - startTime
       

    if rank == 0:
        print("shortest distance:", clusterShortestDistance)
