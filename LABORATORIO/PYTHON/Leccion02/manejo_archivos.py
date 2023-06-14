# Para abrir un archivo declaramos una variable

try:
    archivo = open("prueba.txt", "w", encoding= "utf8")
    archivo.write("Programa con diferentes tipos de archivos, ahora en txt.\n")
    archivo.write("Los acentos son muy importantes para las palabras.\n")
    archivo.write("Como por ejemplo: acción ejecución y producción.\n")
    archivo.write("Las letras son: \nr read leer, \na append anexa,\nw write escribe, \nx crea un archivo")
    archivo.write("\nt esta es opara texto o text, \nb archivos binarios, \nw+ lee y escribe")
    archivo.write("Con esto terminamos\n")

except Exception as e:
    print(e)
finally:  # siempre se ejecuta

    archivo.close()  # Este comando cierra el archivo
# archivo.write("Todo quedo perfecto!!!") #Error porque el archivo ya esta cerrado
