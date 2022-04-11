from array import array
from GetPath import getRandomPath
from GetPathDistance import getPathDistance
from Greedy import greedy
from Greeting import displayGreeting
from LoadMap import loadMap
from mpi4py import MPI
#https://www.obeythetestinggoat.com/
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

cityCount = 1600
rows, cols = (cityCount, cityCount)
cityMap = [[0 for i in range(cols)] for j in range(rows)]
path = [0 for i in range(cols)]
if rank == 0:
    displayGreeting()


cityMap = loadMap(cityCount, cityMap)
greedy(path,cityMap)
