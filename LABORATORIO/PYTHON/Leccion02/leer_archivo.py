try:
    archivo = open("D:\\TecnicaturaOK\\3° Semestre\\Tecnicatura3py\\Archivos\\Leccion02\\prueba.txt", "r", encoding="utf8")
#print(archivo.read(30))
#print(archivo.read(10))
#print(archivo.readline())
#print(archivo.readline())

#vamos a iterar el archivo, cada una de las lineas
#for linea in archivo:
    #print(linea): Iteramos todos los elementos del archivo
    #print(archivo.readlines()): Accedemos al archivo como si fuera una lista
#print(archivo.readlines()) #Accedemos al archivo como si fuera una lista

#Anexamos informacion, copiamos a otro archivos
    archivo2 = open("copia.txt","w", encoding="utf8")
    archivo2.write(archivo.read())
    archivo.close() #Cerramos el primer archivo
    archivo2.close()

    print("Se ha terminado el proceso de leer y copiar archivos")

except Exception as e:
    print(e)
finally:
    print("FIN")