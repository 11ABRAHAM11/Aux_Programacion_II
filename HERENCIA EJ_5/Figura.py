from abc import ABC, abstractmethod

class Figura(ABC):

    def __init__(self, color):
        self.color = color

    @abstractmethod
    def obtener_area(self):
        pass