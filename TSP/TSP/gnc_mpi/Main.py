from array import array
#from Greedy import greedy
from GuessAndCheck import guessAndCheck
from LoadMap import loadMap
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if (rank == 0):
    print("Welcome to Arianna's Shortest Path program. \nWorking through Guess-and-Check.")
#print("Hi from process %d of %d" % (rank, size))
cityCount = 600
if (rank == 0):
    print("Our city count is", cityCount)
path = [0 for i in range(cityCount)]

cityMap = loadMap(cityCount)
guessAndCheck(path, cityMap)
#greedy(path, cityMap)
