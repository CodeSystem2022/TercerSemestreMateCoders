
#para leer informacion de un archivo 'r'
# cuando el archivo esta en otro lugar, se pone \\ en ves de \ para no que lo tome como caracter
# archivo = open('c:\\prueba.txt','r', encoding='utf8')
archivo = open('prueba.txt','r', encoding='utf8')
# print(archivo.read())
#print(archivo.read(16))
#print(archivo.read(10)) # continuamos desde la linea anterior
#print(archivo.readline()) # lee lineas
#print(archivo.readline()) # lee lineas

# vamos a iterar el archivo, cada una de las lineas
#for linea in archivo:
    # print(linea)
#print(archivo.readlines()) # lo pasa como una lista
#print(archivo.readlines()[3])

#ANEXAMOS INFORMACION, COPIAMOS A OTRO
archivo2 = open('copia.txt', 'w', encoding='utf8')
archivo2.write(archivo.read())
archivo.close() # cerramos el primer archivo
archivo2.close()
print('Se ha terminado el proceso de leer y copiar archivos')