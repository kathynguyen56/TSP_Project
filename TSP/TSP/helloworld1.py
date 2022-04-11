#!/usr/bin/env python
"""
Parallel Hello World
"""

from mpi4py import MPI
import sys

size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
name = MPI.Get_processor_name()

sys.stdout.write(
    "Hello, World! I am process %d of %d on %s.\n"
    % (rank, size, name))

sys.stdout.write(
    "What's up! I am process %d of %d on %s.\n"
    % (rank, size, name))

if (0 == rank):
	sys.stdout.write("I am the head node.")

else:
	sys.stdout.write("I am not the head node.")
