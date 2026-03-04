# ============================
# CLASE TELEVISOR
# ============================

class Televisor:
    def __init__(self, marca="", resolucion=0, tipo=""):
        self.__marca = marca
        self.__resolucion = resolucion
        self.__tipo = tipo

    # Getters
    def get_marca(self):
        return self.__marca

    # Setters
    def set_marca(self, marca):
        self.__marca = marca

    def __str__(self):
        return f"Televisor: {self.__marca} | Resolución: {self.__resolucion}p | Tipo: {self.__tipo}"


if __name__ == "__main__":
    # Crear 2 objetos Televisor
    tv1 = Televisor("Samsung", 1080, "LED")
    tv2 = Televisor("LG", 2160, "IPS")

    print(tv1)
    print(tv2)