from animal import Animal

class Cocodrilo(Animal):
    def __init__(self):
        super().__init__()
        self.velocidadnadar = None
        self.nombre = "Federico"
        self.edad = 50
        self.peso = 950
        self.clase = "Réptil"
        self.distancia = 50.6
    
    def natación(self):
        pass