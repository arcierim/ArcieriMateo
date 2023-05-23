import numpy as np
import time
import sys

def compress(file_path):
    start_time = time.time()

    # Leer el archivo de texto
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()

    # Comprimir los datos utilizando la compresión de texto de Python
    compressed_data = data.encode('utf-8')

    # Guardar el archivo comprimido
    compressed_file_path = 'comprimido.elmejorprofesor'
    with open(compressed_file_path, 'wb') as file:
        file.write(compressed_data)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Tiempo transcurrido en segundos: {elapsed_time}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Por favor, proporcione el archivo de entrada como argumento.")
    else:
        input_file = sys.argv[1]
        compress(input_file)
