from animal import Animal

#Recuerdo de que con "()" se indicala herencia.
class Delfin(Animal):
    def __init__(self):
        super().__init__()
        self.iq = None
        self.raza = "Nariz de botella"
        self.edad = 11
        self.peso = 500
        self.clase = "mamífero"
        self.distancia = 132.5