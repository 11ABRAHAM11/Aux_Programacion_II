from Figura import Figura
import math

class Triangulo(Figura):

    def __init__(self, color, lado1, lado2, lado3):
        super().__init__(color)
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def obtener_area(self):
        # Fórmula de Herón
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        area = math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))
        return area