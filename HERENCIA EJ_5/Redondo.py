from Figura import Figura
import math

class Redondo(Figura):

    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio

    def obtener_area(self):
        return math.pi * (self.radio ** 2)