from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
    
#numCities = 12
#currentShortestPath = [0 for i in range(size)]

#currentShortestPath[rank] += rank
#print(rank, currentShortestPath)

#comm.barrier


#if rank == 0:
#    data = np.arange(size, dtype='i')
#else:
#    data = np.empty(size, dtype='i')
#comm.Bcast(data, root=0)
#assert data[rank] == rank
#print(rank, currentShortestPath[rank])

#comm.barrier

if rank == 0:
    print ("Start of broadcasting integer")
    
comm.barrier

if rank == 0:
    distance = 0
    
else:
    distance = None
    
distance = comm.bcast(distance, root=0)

comm.barrier
#print(rank, distance)

distance += rank
print(rank, distance, "after adding")
    
maxDistance = comm.reduce(distance, op=MPI.MAX, root=0)
if rank == 0:
    print (rank, maxDistance, "is max")
    
distance = comm.bcast(maxDistance, root=0)
print(rank, distance, "is new value")
