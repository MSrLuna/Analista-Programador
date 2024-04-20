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
        # la siguiente línea es equivalente a la anterior. Nos sirve para evitar volver
        # a escribir el nombre de la variable que está siendo auto sumada
        #self.distancia += kms
        if (kms > 10):
            self.peso = self.peso - 1
            #self.peso -= 1

    def comer(self, kgs):
        # con esto obtenemos el 5% del peso del animal
        peso5porCiento = self.peso * 0.05
        # ahora comparamos si lo comido es superior a ese 5% de peso del animal
        if (kgs > peso5porCiento):
            # si el animal devuelve el 90% de lo que comió, es lo mismo a decir
            # que el animal solo ganó de peso el 10% de lo ingerido
            pesoGanado = kgs * 0.1
            self.peso = self.peso + pesoGanado
        else:
            self.peso = self.peso + kgs
    
    def mostrarDatos(self):
        return f"Nombre: {self.nombre}, Peso: {self.peso}, Distancia: {self.distancia}"
    