from Biblioteca import Biblioteca
from Libro import Libro

def main():

    b1 = Biblioteca("Central")
    b2 = Biblioteca("Zona Sur")

    b1.agregar_libro(Libro("Java", "Autor1", 2020))
    b1.agregar_libro(Libro("Python", "Autor2", 2021))

    b2.agregar_libro(Libro("C++", "Autor3", 2019))
    b2.agregar_libro(Libro("Java", "Autor4", 2018))

    nombre = input("Ingrese nombre del libro: ")
    b1.buscar_libro(nombre)
    b2.buscar_libro(nombre)

    max_libros = max(b1.cantLibros, b2.cantLibros)

    print("\nBiblioteca(s) con mayor cantidad:")
    if b1.cantLibros == max_libros:
        b1.mostrar()

    if b2.cantLibros == max_libros:
        b2.mostrar()

if __name__ == "__main__":
    main()