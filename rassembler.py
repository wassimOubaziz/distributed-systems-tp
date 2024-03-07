from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

line = np.full(size, rank)
table = np.zeros((size, size), dtype=int)

print(line)
print(rank,table)
comm.Allgather([line, MPI.INT], [table, MPI.INT])
print(rank,table)