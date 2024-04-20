class Animal:
    def __init__(self):
        self.nombre = None
        self.raza = None
        self.edad = None
        self.peso = None
        self.clase = None
        self.distancia = None

    def avanzar(self, kms):

        self.distancia = self.distancia + kms
        self.distancia += kms

        if  kms > 10:

            self.peso = self.peso - 1
            self.peso -= 1

    def comer(self, kgs):

        self.peso = self.peso + kgs
        self.peso += kgs

        porcentajepeso = self.peso * (5/100)
        if kgs > porcentajepeso:
            quitarpeso = kgs * (90/100)

            self.peso = self.peso - quitarpeso
            self.peso -= quitarpeso