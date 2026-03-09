class Fraccion:

    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def multiplica(self, o):
        num = self.numerador * o.numerador
        den = self.denominador * o.denominador
        return Fraccion(num, den)

    def divide(self, o):
        num = self.numerador * o.denominador
        den = self.denominador * o.numerador
        return Fraccion(num, den)


# prueba
f1 = Fraccion(2,3)
f2 = Fraccion(4,5)

r1 = f1.multiplica(f2)
r2 = f1.divide(f2)

print("Multiplicación:", r1.numerador, "/", r1.denominador)
print("División:", r2.numerador, "/", r2.denominador)