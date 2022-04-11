from mpi4py import MPI
import random

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
name = MPI.Get_processor_name() 

jobsPerWorker = 10

if rank == 0:
	print("Hi, I'm the head node's 1st processor.")
	print("My workers are going to generate some numbers.")
	print("Then I'll compare the numbers to find the highest one.")

else:
	myArr = [0 for i in range(jobsPerWorker)]
	for i in range(len(myArr)):
		myArr[i] = random.randint(0, 10000)
		comm.send(myArr[i], dest=0) 
	print("Worker", rank, ":", myArr)

if rank == 0:
	highestNum = 0
	highestNumIndex = 0
	results = [0 for i in range(size * jobsPerWorker)]
	for i in range(1, size):
		for j in range(i * jobsPerWorker, (i * jobsPerWorker) + jobsPerWorker):
			results[j] = comm.recv(source=i)

	for i in range(len(results)):
		if results[i] > highestNum:
			highestNum = results[i]
			highestNumIndex = i

	print("Highest roll was %d from worker %d." % (highestNum, (highestNumIndex // 4)))

