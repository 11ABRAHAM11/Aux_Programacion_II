class Edificio:
    def __init__(self, nombre, superficie):
        self.__nombre = nombre
        self.__superficie = superficie
        self.__departamentos = []
        self.__parqueo = None

    def adicionarParqueo(self, parqueo):
        self.__parqueo = parqueo

    def agregarDepartamento(self, dep):
        self.__departamentos.append(dep)

    def mostrarMayorHabitacionesPiso(self, y):
        mayor = 0
        elegido = None

        for d in self.__departamentos:
            if d.getPiso() == y:
                if d.cantidadHabitaciones() > mayor:
                    mayor = d.cantidadHabitaciones()
                    elegido = d

        if elegido:
            print("Departamento con más habitaciones:")
            print(elegido)

    def agregarMuebleDepartamento(self, z, x, mueble):
        for d in self.__departamentos:
            if d.getPuerta() == z and d.getPiso() == x:
                d.agregarMueble(mueble)
    def mostrarDepartamentoMasMuebles(self):
        mayor = 0

        for d in self.__departamentos:
            if d.cantidadMuebles() > mayor:
                mayor = d.cantidadMuebles()

        print("Departamento(s) con más muebles:")
        for d in self.__departamentos:
            if d.cantidadMuebles() == mayor:
                print(d)

    def mostrarHabitacionMasMueblesPiso(self, z):
        print("Habitación con más muebles del piso", z)

        for d in self.__departamentos:
            if d.getPiso() == z:
                print(d.habitacionMayorMuebles())

    def esPrimo(self, n):
        if n < 2:
            return False

        for i in range(2, n):
            if n % i == 0:
                return False

        return True

    def eliminarDepartamentosPrimos(self):
        nueva = []

        for d in self.__departamentos:
            if not self.esPrimo(d.cantidadHabitaciones()):
                nueva.append(d)

        self.__departamentos = nueva

    def mostrar(self):
        print("EDIFICIO:", self.__nombre)
        for d in self.__departamentos:
            print(d)