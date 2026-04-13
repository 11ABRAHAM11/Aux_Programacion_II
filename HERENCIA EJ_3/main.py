from Estudiante import Estudiante
from Docente import Docente

# FUNCIÓN
def misma_edad(estudiante, docente):
    return estudiante.edad == docente.edad

# PROCEDIMIENTO
def verificar_edades(e1, e2, d):
    if misma_edad(e1, d):
        print("El estudiante 1 tiene la misma edad que el docente")
    if misma_edad(e2, d):
        print("El estudiante 2 tiene la misma edad que el docente")


# MAIN
if __name__ == "__main__":  

    e1 = Estudiante("Juan", 123, 20, 1001, "Sistemas")
    e2 = Estudiante("Ana", 456, 25, 1002, "Sistemas")
    d1 = Docente("Carlos", 789, 25, 10, 3500)

    e1.mostrar()
    e2.mostrar()
    d1.mostrar()

    verificar_edades(e1, e2, d1)

    if e1.misma_carrera(e2):
        print("Los estudiantes están en la misma carrera")
    else:
        print("Los estudiantes NO están en la misma carrera")