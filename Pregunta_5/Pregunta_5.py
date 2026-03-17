class Aula:

    def __init__(self, nombre_aula, piso, matriz_estudiantes):
        self.nombre_aula = nombre_aula
        self.piso = piso
        self.matriz_estudiantes = matriz_estudiantes


    def mostrarEstudiantes(self):
        print("Aula:", self.nombre_aula)
        print("Piso:", self.piso)
        print("Estudiantes y notas:")

        for estudiante in self.matriz_estudiantes:
            print(estudiante[0], estudiante[1])


# matriz de estudiantes
estudiantes = [
    ["Luis", 67],
    ["Aracely", 89]
]


# crear objeto Aula
aula1 = Aula("Aula 101", 2, estudiantes)


# mostrar datos
aula1.mostrarEstudiantes()