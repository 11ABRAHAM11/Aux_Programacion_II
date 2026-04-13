from Persona import Persona

class Estudiante(Persona):

    def __init__(self, nombre, carnet, edad, matricula, carrera):
        super().__init__(nombre, carnet, edad)
        self.matricula = matricula
        self.carrera = carrera

    def mostrar(self):
        super().mostrar()
        print("Matricula:", self.matricula)
        print("Carrera:", self.carrera)
        print("----------------------")

    # Método para verificar misma carrera
    def misma_carrera(self, otro):
        return self.carrera == otro.carrera