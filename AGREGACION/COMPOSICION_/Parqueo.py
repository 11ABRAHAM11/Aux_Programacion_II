class Parqueo:
    def __init__(self, capacidad, precioH):
        self.__capacidad = capacidad
        self.__precioH = precioH
        self.__placas = []

    def agregarAuto(self, placa):
        self.__placas.append(placa)

    def __str__(self):
        return "Capacidad: " + str(self.__capacidad)
