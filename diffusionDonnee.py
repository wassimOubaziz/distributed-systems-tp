from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD

rank = comm.Get_rank()
data = np.zeros(3, dtype=int)

if rank == 0:
    data = np.arange(1,10,3)

print('avant envoi le contenu de data est :', data)
data= comm.bcast(data, root=0)
print(str(rank), "le contenu apres reception :", data)