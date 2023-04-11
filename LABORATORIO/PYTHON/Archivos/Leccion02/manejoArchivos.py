class manejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        print('Obtenemos el recurso'.center(50,'-'))
        self.nombre = open(self.nombre, 'r', encoding='utf8')
        return self.nombre

    def __exit__(self, tipo_excepcion, valor_excepcion, traza_error):
        print('cerramos el recurso'.center(50,'_'))
        if self.nombre:
            self.nombre.close()# cerramos el archivo

