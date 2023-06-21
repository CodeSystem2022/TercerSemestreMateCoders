import json

asientos = {}
letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # Letras de las columnas

num_filas = 15
num_columnas = 20

for fila in range(1, num_filas + 1):
    for columna in range(num_columnas):
        letra = letras[columna]
        asiento = f'{letra}{fila}'
        asientos[asiento] = False

print(asientos)

with open('sala.JSON', 'w') as file:
    json.dump(asientos, file)
