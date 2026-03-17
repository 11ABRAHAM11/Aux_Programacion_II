class Videojuego:

    # b) Sobrecarga del constructor (2 formas)
    def __init__(self, nombre, plataforma, jugadores=None):

        # constructor 1
        if isinstance(nombre, str) and isinstance(plataforma, str) and jugadores is None:
            self.nombre = nombre
            self.plataforma = plataforma
            self.jugadores = 1

        # constructor 2
        elif isinstance(nombre, str) and isinstance(plataforma, str) and isinstance(jugadores, int):
            self.nombre = nombre
            self.plataforma = plataforma
            self.jugadores = jugadores


    # c) Sobrecarga del método agregarJugadores
    def agregarJugadores(self, cantidad=None):

        # agregar solo 1 jugador
        if cantidad is None:
            self.jugadores += 1

        # agregar n jugadores
        elif isinstance(cantidad, int):
            self.jugadores += cantidad


# a) Instanciar 2 videojuegos
juego1 = Videojuego("FIFA 24", "PC")
juego2 = Videojuego("Mario Kart", "Switch", 4)

print("Estado inicial")
print(juego1.nombre, juego1.plataforma, juego1.jugadores)
print(juego2.nombre, juego2.plataforma, juego2.jugadores)

# agregar 1 jugador
juego1.agregarJugadores()

# agregar n jugadores por teclado
n = int(input("Cantidad de jugadores a agregar: "))
juego2.agregarJugadores(n)

print("Estado final")
print(juego1.nombre, juego1.jugadores)
print(juego2.nombre, juego2.jugadores)