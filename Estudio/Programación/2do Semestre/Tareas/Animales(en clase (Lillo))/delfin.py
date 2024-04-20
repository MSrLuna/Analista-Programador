from animal import Animal
class Delfin(Animal):

    def __init__(self):
        super().__init__()
        self.iq = None
        self.raza = "Nariz de Botella"
        self.edad = 11
        self.peso = 500
        self.clase = "Mamífero"
        self.distancia = 132.5
    
    def nadar(self):
        pass