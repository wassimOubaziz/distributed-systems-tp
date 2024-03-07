from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# Assuming you want to generate size * 3 random integers on root process
if rank == 0:
    data = np.random.randint(0, 20, size*3)
else:
    data = None

# Scatter the data
rcvdata = np.empty(3, dtype=int)
comm.Scatter(data, rcvdata, root=0)

# Calculate local mean
local_mean = np.mean(rcvdata)

# Gather local means on root process
gathered_means = comm.gather(local_mean, root=0)

# Root process calculates the global mean
if rank == 0:
    global_mean = np.mean(gathered_means)
    print("Global mean:", global_mean)
