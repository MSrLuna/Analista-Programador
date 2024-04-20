class Animal:
    def __init__(self):
        self.nombre = None
        self.raza = None
        self.edad = None
        self.peso = None
        self.clase = None
        self.distancia = None

    def avanzar(self, kms):
        print(f"{self.nombre} avanza {kms}kms...")
        self.distancia += kms
        print()
        print(f"{self.nombre} ha avanzado en total {self.distancia}kms.")
        print()
        if kms > 10:
            self.peso -= 1
            print(f"Gracias a ese ejercicio {self.nombre} ha bajado de peso ha {self.peso}kgs (-1kg).")
            print()
    
    def comer(self, kgs):
        print(f"{self.nombre} come {kgs}kgs...")
        pesototal = self.peso + kgs
        print()
        print(f"{self.nombre} sube de peso a {pesototal}kgs...")
        print()
        if kgs > self.peso * 0.05:
            self.peso += kgs * 0.1
            print(f"Oh no, fue demasiado para {self.nombre}, vomitó una parte.")
            print(f"Ahora pesa {self.peso}kgs.")
            print()
        else:
            self.peso += kgs
            print()