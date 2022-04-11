#LoadMap
from BuildMap import buildMap
import numpy as np
import os.path
from os import path
from mpi4py import MPI

def loadMap(cityCount, cityMap, fileName):

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    if (rank == 0):
        loadMapGreeting = f"Hello, we will have {cityCount} cities"
        print(loadMapGreeting)
    #fileName = f"spp{cityCount}.bin"
    if (rank == 0):    
        print("We want to open file:", fileName)
    if(path.exists(fileName)):
        if (rank == 0): 
            print ("File exists")
        cityMap = np.fromfile(fileName,  dtype=np.int, count = -1)
        cityMap = np.reshape(cityMap,(cityCount,cityCount))
        #if (rank == 0): 
            #print(cityMap)
        return cityMap
    else:
        if (rank == 0): 
            print("File does not exist")
            print("Building map.")
        buildMap(cityCount,fileName)
        loadMap(cityCount, cityMap)
