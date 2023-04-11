# con with lo abre y lo cierra: sintaxis simplificada
#with open('prueba.txt', 'r', encoding='utf8') as archivo:
#    print(archivo.read())

# no hace falta el try, ni el finally
# en el contexto de eith lo que se ejecuta de manera automatica
# utiliza diferentes metodos: __enter__ este es el que abre
# Ahora el siguiente metodo es el qie cierra: __exit__
from manejoArchivos import manejoArchivos

with manejoArchivos('prueba.txt') as archivo:
    print(archivo.read())