from GetPath import getRandomPath
from GetPathDistance import getPathDistance
import time
from mpi4py import MPI


def guessAndCheck(path,cityMap):
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()
    runTime = 300
    clock = 0.0
    tempDistance = 0
    shortestDistance = 0
    winner = 0

    if (rank == 0):
        print("Start of guess-and-check algorithm. Running for %d seconds." % (runTime))

    tempPath = [0 for i in range(len(path))]

    if (rank == 0):
        getRandomPath(tempPath)
        shortestDistance = getPathDistance(tempPath,cityMap)
        winner = shortestDistance

    shortestDistance = comm.bcast(shortestDistance, root=0)
    
    comm.Barrier()
    startTime = time.time()
    
    while (clock < runTime - 2.0):
        
        getRandomPath(tempPath)
        tempDistance = getPathDistance(tempPath,cityMap)
        tempDistance = tempDistance - 200

        if (tempDistance < shortestDistance):
            shortestDistance = tempDistance
            path = tempPath.copy

        stopTime = time.time()
        clock = stopTime - startTime

    print("shortest distance:", shortestDistance, "from process", rank)
