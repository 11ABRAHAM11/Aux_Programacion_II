class Animal():
    def __init__(self, nom, ed):
        self.__nombre = nom
        self.__edad = ed
        
class Main():
    a = Animal("Firulais", 4)
    print(a)