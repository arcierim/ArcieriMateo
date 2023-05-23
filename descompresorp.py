import numpy as np
import sys
from mpi4py import MPI

def decompress(compressed_file_path, output_file_path):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    
    if rank == 0:
        compressed_data = np.load(compressed_file_path, mmap_mode='r')
        data_size = len(compressed_data)
    else:
        compressed_data = None
        data_size = None

    
    data_size = comm.bcast(data_size, root=0)

    
    chunk_size = data_size // size
    remainder = data_size % size

    
    sizes = [chunk_size if i < size - 1 else chunk_size + remainder for i in range(size)]
    displacements = [sum(sizes[:i]) for i in range(size)]

    
    receive_buffer = np.empty(sizes[rank], dtype=np.uint8)

    
    comm.Scatterv([compressed_data, sizes, displacements, MPI.BYTE], receive_buffer, root=0)

   
    gathered_data = comm.gather(receive_buffer, root=0)

    
    if rank == 0:
        flattened_data = np.concatenate(gathered_data)
        text = flattened_data.tobytes().decode('utf-8')
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(text)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Por favor, proporcione el archivo comprimido y el nombre del archivo de salida como argumentos.")
    else:
        compressed_file = sys.argv[1]
        output_file = sys.argv[2]
        decompress(compressed_file, output_file)
