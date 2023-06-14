from ManejoArchivos import ManejoArchivos
#Manejo de contexto with
#with open("prueba.txt", "r", encoding="utf8") as archivo:
#    print(archivo.read())
#No hace falta ni el try, ni el finally
#En el contexto de with lo que se ejecuta de manera automatica
# Utiliza diferentes metodos: __enter__ es el que abre
#otro metod es __exit__ que es el que cierra.

with ManejoArchivos("prueba.txt") as archivo:
    print(archivo.read())

