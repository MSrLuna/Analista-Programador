from animal import Animal

#Recuerdo de que con "()" se indicala herencia.
class Canguro(Animal):
    def __init__(self):
        #super() está llamando a la clase padre... su a través de super llamamos a
        #__init__(),entonces podemos entender que está llamando al constructor de la
        #clase padre.
        self.fuerzagolpe = None
        self.edad = 5
        self.peso = 25
        self.clase = "mamífero"
        self.distancia = 32.5

    def boxear(self):
        pass