import numpy as np
import sys
from mpi4py import MPI

def compress(input_file_path, compressed_file_path):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0:
        with open(input_file_path, 'r', encoding='utf-8') as file:
            data = file.read().encode('utf-8')
        data_size = len(data)
    else:
        data = None
        data_size = None

    data_size = comm.bcast(data_size, root=0)

    chunk_size = data_size // size
    remainder = data_size % size

   
    sizes = [chunk_size if i < size - 1 else chunk_size + remainder for i in range(size)]
    displacements = [sum(sizes[:i]) for i in range(size)]

  
    data_chunk = np.empty(sizes[rank], dtype=np.uint8)
    comm.Scatterv([data, sizes, displacements, MPI.BYTE], data_chunk, root=0)

   
    compressed_data = np.array([char.item() for char in data_chunk], dtype=np.uint8)

   
    gathered_data = comm.gather(compressed_data, root=0)

   
    if rank == 0:
        flattened_data = np.concatenate(gathered_data)
        np.save(compressed_file_path, flattened_data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Por favor, proporcione el archivo de entrada como argumento.")
    else:
        input_file = sys.argv[1]
        compressed_file = "comprimidop.elmejorprofesor"
        compress(input_file, compressed_file)
