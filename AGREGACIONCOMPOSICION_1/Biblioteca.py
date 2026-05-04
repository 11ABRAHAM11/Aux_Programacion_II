from Libro import Libro

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        self.cantLibros = 0

    def agregar_libro(self, libro):
        if self.cantLibros < 100:
            self.libros.append(libro)
            self.cantLibros += 1

    def buscar_libro(self, nombre):
        encontrado = False

        for libro in self.libros:
            if libro.nombre.lower() == nombre.lower():
                libro.mostrar()
                encontrado = True

        if not encontrado:
            print(f"No encontrado en {self.nombre}")

    def mostrar(self):
        print(f"\nBiblioteca: {self.nombre}")
        print(f"Cantidad: {self.cantLibros}")
        for libro in self.libros:
            libro.mostrar()