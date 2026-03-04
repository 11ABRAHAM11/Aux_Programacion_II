# ============================
# CLASE INSTRUMENTO
# ============================

class Instrumento:
    def __init__(self, nombre, material, tipo):
        self.nombre = nombre
        self.__material = material
        self.__tipo = tipo

    # Getters
    def get_material(self):
        return self.__material

    def get_tipo(self):
        return self.__tipo

    # Setters
    def set_material(self, material):
        self.__material = material

    def set_tipo(self, tipo):
        self.__tipo = tipo

    def __str__(self):
        return f"Instrumento: {self.nombre} | Material: {self.__material} | Tipo: {self.__tipo}"


if __name__ == "__main__":
    # Crear 2 objetos Instrumento
    inst1 = Instrumento("Guitarra", "Madera", "Cuerda")
    inst2 = Instrumento("Flauta", "Metal", "Aire")

    print(inst1)
    print(inst2)