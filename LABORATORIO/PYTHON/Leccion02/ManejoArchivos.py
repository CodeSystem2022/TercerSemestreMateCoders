class ManejoArchivos:
    def __init__(self, name): #Para obtener el nombre del archivo
        self.name = name

    def __enter__(self):
        print("Obtenemos el recurso".center(50, "-"))
        self.name = open(self.name, "r", encoding="utf8")#Encapsulamos el codigo dentro del metodo main
        return self.name

    def __exit__(self, tipo_exception, valor_exception, traza_error):
        print("cerramos el recurso".center(50, "-"))
        if self.name:
            self.name.close()#Cerramos el archivo