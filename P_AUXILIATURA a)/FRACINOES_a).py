class Fraccion:

    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    # inciso a
    def multiplica(self, o):
        num = self.numerador * o.numerador
        den = self.denominador * o.denominador
        return Fraccion(num, den)


# probar el método
f1 = Fraccion(2,3)
f2 = Fraccion(4,5)

resultado = f1.multiplica(f2)

print(resultado.numerador, "/", resultado.denominador)