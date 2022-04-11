import numpy as np
import random
from mpi4py import MPI

def buildMap(cityCount, fileName):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    
    if (rank == 0):
        print("We are going to build a map for", cityCount, "cities.")
    rows, cols = (cityCount, cityCount)
    cityMap = [[0 for i in range(cols)] for j in range(rows)]

    for rowIndex in range(rows):
        for columnIndex in range(cols):
            cityMap[rowIndex][columnIndex] = random.randint(10,99)

#    if (rank == 0):
#        print(cityMap)
    np.array(cityMap).tofile(fileName)
