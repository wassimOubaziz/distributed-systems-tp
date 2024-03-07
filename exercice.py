from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

arr = np.zeros(10)

if rank == 0:
    arr[rank] = rank
    comm.Send(arr, dest=1)
    comm.Recv(arr, source=size-1) 
    print("fid de l'echange: ", arr)  

else:
    comm.Recv(arr, source=(rank - 1))
    arr[rank] = rank
    comm.Send(arr, dest=((rank + 1) % size))
