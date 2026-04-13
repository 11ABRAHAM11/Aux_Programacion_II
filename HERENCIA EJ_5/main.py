from Cuadrado import Cuadrado
from Triangulo import Triangulo
from Redondo import Redondo

c1 = Cuadrado("Rojo", 4)
c2 = Cuadrado("Azul", 6)

t1 = Triangulo("Verde", 3, 4, 5)
t2 = Triangulo("Amarillo", 5, 5, 6)

r1 = Redondo("Negro", 3)
r2 = Redondo("Blanco", 5)

figuras = [c1, c2, t1, t2, r1, r2]

for f in figuras:
    print("Color:", f.color)
    print("Área:", f.obtener_area())
    print("----------------------")

if c1.obtener_area() > t1.obtener_area():
    print("Mayor área: Cuadrado → Color:", c1.color)
else:
    print("Mayor área: Triángulo → Color:", t1.color)