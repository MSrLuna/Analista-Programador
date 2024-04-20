from animal import Animal

class Pollo(Animal):
    def __init__(self):
        super().__init__()
        self.ponerhuevo = None
        self.nombre = "Pío"
        self.raza = "Broiler"
        self.edad = 2
        self.peso = 4.3
        self.clase = "Ave"
        self.distancia = 5.2

    def ponerhuevo(self):
        pass