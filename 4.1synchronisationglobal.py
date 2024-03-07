from mpi4py import MPI

comm = MPI.COMM_WORLD

rank = comm.Get_rank()

if rank == 0:
    print("processus", rank, "commence son execution")
comm.Barrier()

print('processus', rank, 'a atteint la barriere')