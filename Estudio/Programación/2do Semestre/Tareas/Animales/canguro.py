from animal import Animal

class Canguro(Animal):
    def __init__(self):
        super().__init__()
        self.nombre = "Gilberto"
        self.edad = 5
        self.peso = 25
        self.clase = "Mamífero"
        self.distancia = 32.5