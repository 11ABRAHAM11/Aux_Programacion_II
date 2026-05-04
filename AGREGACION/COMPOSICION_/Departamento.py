class Departamento:
    def __init__(self, nroPuerta, nroPiso):
        self.__nroPuerta = nroPuerta
        self.__nroPiso = nroPiso
        self.__habitaciones = []

    def agregarHabitacion(self, hab):
        self.__habitaciones.append(hab)

    def getPuerta(self):
        return self.__nroPuerta

    def getPiso(self):
        return self.__nroPiso

    def cantidadHabitaciones(self):
        return len(self.__habitaciones)

    def cantidadMuebles(self):
        total = 0
        for h in self.__habitaciones:
            total += h.cantidadMuebles()
        return total

    def agregarMueble(self, mueble):
        if len(self.__habitaciones) > 0:
            self.__habitaciones[0].agregarMueble(mueble)

    def habitacionMayorMuebles(self):
        mayor = self.__habitaciones[0]
        for h in self.__habitaciones:
            if h.cantidadMuebles() > mayor.cantidadMuebles():
                mayor = h
        return mayor

    def __str__(self):
        return "Puerta: " + str(self.__nroPuerta) + " Piso: " + str(self.__nroPiso)
