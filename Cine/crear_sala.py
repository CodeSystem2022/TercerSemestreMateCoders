import json

asientos = {}
letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # Letras de las columnas

num_filas = 15
num_columnas = 15

for fila in range(num_filas):
    letra = letras[fila]
    for columna in range(1, num_columnas + 1):
        asiento = f'{columna}{letra}'
        asientos[asiento] = False

print(asientos)

with open('Cine/sala.JSON', 'w') as file:
    json.dump(asientos, file)
