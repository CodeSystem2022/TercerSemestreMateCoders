# Declaramos una variable
try:# con open agregamos una carpeta o la abrimos
    archivo = open('prueba.txt', 'w', encoding='utf8') # La w es de write que significa escribir
    # con el metodo write escribimos
    archivo.write('Programamos con diferentes tipos de archivos, ahora en txt.\n')
    archivo.write('Los acentos son importantes para las palabras\n')
    archivo.write('como por ejemplo: acción, ejecución y producción\n')
    archivo.write('las letras son:\n r read leer,\n a append anexa,\n w write escribe,\n x crea un archivo\n')
    archivo.write(' t esta es para texto o text, \n b archivos binarios, \nw+ lee y escribe son iguales a r+ \n')
    archivo.write('saludo a todos los alumnos\n')
    archivo.write('Con esto terminamos')
except Exception as e:
    print(e)
finally: # siempre se ejecuta
    archivo.close() # con esto se debe cerrar el archivo
#     archivo.write('Con esto terminamos') este es un error por que despues de finallyy ya cerro el archivo
