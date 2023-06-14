# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 20:53:37 2023

@author: dania
"""

archivo = open('prueba.txt','r')
#print(archivo.read())

# print(archivo.read(15)) #muestra las 15 primeras letras

# print(archivo.read(5)) #continúa con las 5 siguientes letras

#podemos leer una línea completa:
    
# print(archivo.readline()) #lee la primer línea

# otras letras que se pueden agregar son 'a' - append, 
# 'x' - crea un archivo si no existe el archivo, manda una excepción
# 't' - es para texto o text 'b' - para archivos de tipo binario
# 'w+' - es un modo combinado, lo vamos a usar para escribir y ller información
# 'r+' - para leer y escribir

#Otra cosa a tener en cuenta es la ruta donde está el archivo
#si está en la misma carpeta del .py, no es necesario aclarar nada
# si no, hay que espcificar antes del archivo, la ruta (ver video clase 2 parte 7)

#Vamos a iterar las líneas del archivo

# for linea in archivo:
    #print(linea) #itera mostrando línea por línea
    
    # print(archivo.readlines()) # arma una lista con las líneas

#o podemos pedirle una sola línea:
# print(archivo.readlines()[0])

#Vamos a anexar información al archivo usando 'a', creando además el archivo

archivo3 = open('copia.txt','a')
archivo3.write(archivo.read())
archivo.close()
archivo3.close()

print('Se ha terminado el proceso de leer y copiar archivos')
