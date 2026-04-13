from Figura import Figura

class Cuadrado(Figura):

    def __init__(self, color, lado):
        super().__init__(color)
        self.lado = lado

    def obtener_area(self):
        return self.lado * self.lado