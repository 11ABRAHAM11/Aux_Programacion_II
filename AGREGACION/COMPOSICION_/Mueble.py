class Mueble:
    def __init__(self, tipo, material):
        self.__tipo = tipo
        self.__material = material

    def getTipo(self):
        return self.__tipo

    def __str__(self):
        return self.__tipo + " - " + self.__material
