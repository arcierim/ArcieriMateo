import sys
from mpi4py import MPI

def verify(file1_path, file2_path):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    with open(file1_path, 'r', encoding='utf-8') as file1:
        data1 = file1.read()

    with open(file2_path, 'r', encoding='utf-8') as file2:
        data2 = file2.read()

    if data1 == data2:
        result = "ok"
    else:
        result = "nok"

    # Reunir los resultados de todos los procesos en el proceso 0
    all_results = comm.gather(result, root=0)

    # Imprimir el resultado solo en el proceso 0
    if rank == 0:
        if all_results.count("nok") > 0:
            print("nok")
        else:
            print("ok")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Por favor, proporcione dos archivos para comparar.")
    else:
        file1 = sys.argv[1]
        file2 = sys.argv[2]
        verify(file1, file2)
