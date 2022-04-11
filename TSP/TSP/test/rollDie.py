from mpi4py import MPI
import random

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
name = MPI.Get_processor_name() 

if rank == 0:
	print("Hi, I'm the head node's 1st processor.")
	print("My workers are going to generate some numbers.")
	print("Then I'll compare the numbers to find the highest one.")
	rolls = [0 for i in range(size * 4)]
	print("Sending array...")
	for i in range(1, size):
		comm.send(rolls, dest=i)

else:
	rolls = comm.recv(source=0)
	indexStart = rank * 4
	indexFinish = indexStart + 4
	for i in range(indexStart, indexFinish):
		rolls[i] = random.randint(0, 10000)
		comm.send(rolls[i], dest=0) 
	print("worker", rank, "numbers:", rolls[indexStart], rolls[indexStart + 1], rolls[indexStart + 2], rolls[indexStart + 3])
#	for i in range(indexStart, indexFinish):
		

if rank == 0:
	high = 0
	highPlace = 0
	for i in range(1, size):
		for j in range(i * 4, (i * 4) + 4):
			rolls[j] = comm.recv(source=i)

	for i in range(len(rolls)):
		if rolls[i] > high:
			high = rolls[i]
			highPlace = i

	print("Highest roll was", high, "from worker", (highPlace // 4))

