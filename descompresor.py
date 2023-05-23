import time
import sys

def decompress(compressed_file_path):
    start_time = time.time()

   
    with open(compressed_file_path, 'rb') as file:
        compressed_data = file.read()

   
    data = compressed_data.decode('utf-8')

   
    output_file_path = 'descomprimido-elmejorprofesor.txt'
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(data)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Tiempo transcurrido en segundos: {elapsed_time}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Por favor, proporcione el archivo comprimido como argumento.")
    else:
        compressed_file = sys.argv[1]
        decompress(compressed_file)
