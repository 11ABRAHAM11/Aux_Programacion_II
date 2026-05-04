class Habitacion:
    def __init__(self, nombre, tamanio):
        self.__nombre = nombre
        self.__tamanio = tamanio
        self.__muebles = []

    def agregarMueble(self, mueble):
        self.__muebles.append(mueble)

    def cantidadMuebles(self):
        return len(self.__muebles)

    def getNombre(self):
        return self.__nombre

    def mostrarMuebles(self):
        for x in self.__muebles:
            print(x)

    def __str__(self):
        return self.__nombre + " - Tamaño: " + str(self.__tamanio)
