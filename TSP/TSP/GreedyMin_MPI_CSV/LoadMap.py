#LoadMap
from BuildMap import buildMap
import numpy as np
import os.path
from os import path
from mpi4py import MPI
from numpy import genfromtxt
#https://www.obeythetestinggoat.com/
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()


def loadMap(cityCount, cityMap):
    loadMapGreeting = f"Hello, we will have {cityCount} cities"
    if rank == 0:
        print(loadMapGreeting)
    #fileName = f"spp{cityCount}.bin"
    fileName = f"spp{cityCount}.csv"
    if rank == 0:
        print("We want to open file:", fileName)
    if(path.exists(fileName)):
        if rank == 0:
            print ("File exists")
        cityMap = genfromtxt(fileName, delimiter=',')
        #cityMap = np.fromfile(fileName,  dtype=np.int, count = -1)
        #cityMap = np.reshape(cityMap,(cityCount,cityCount))
#        print(cityMap)
        return cityMap
    else:
        if rank == 0:
            print("File does not exist")
            print("Building map.")
        buildMap(cityCount,fileName)
        loadMap(cityCount, cityMap)
