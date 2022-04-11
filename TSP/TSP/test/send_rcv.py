from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank > 3:
	msg = "Hello, world"
	comm.send(msg, dest=(rank % 4))
elif rank < 4:
	s = comm.recv()
	print ("rank %d: %s" % (rank, s))
