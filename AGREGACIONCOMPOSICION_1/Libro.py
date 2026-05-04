class Libro:
    def __init__(self, nombre, autor, anio):
        self.nombre = nombre
        self.autor = autor
        self.anio = anio

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Autor: {self.autor}")
        print(f"Año: {self.anio}")
        print("----------------------")