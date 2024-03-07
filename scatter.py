from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
data = np.empty([size, 3], dtype=int)


if rank == 0:
    data = np.arange(size*3, dtype=int).reshape(size, 3)
    print(data)
rcvdata = np.zeros(3, dtype=int)
print("valuer avant reception", rcvdata)
comm.Scatter(data, rcvdata, root=0)
print(rank,"valuer apres reception", rcvdata)