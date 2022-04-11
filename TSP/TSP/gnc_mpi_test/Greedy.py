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
    
    print("Hi from process", rank)
    
    
    
    
    
def pickRandomCity(citiesToVisit):



def getGreedyPath(tempPath,citiesToVisit,cityMap):