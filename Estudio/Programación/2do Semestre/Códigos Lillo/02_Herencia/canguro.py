from animal import Animal
# Poniendo entre paréntesis el nombre de una clase, indicamos herencia
class Canguro(Animal):
    
    def __init__(self):
        # super() está llamando a la clase padre.. si a través de super llamamos a
        # __init__(), entonces podemos entender que se está llamando al constructor
        # de la clase padre
        super().__init__()
        self.fuerzaGolpe = None
        # si definimos un valor para algún atributo, entonces SIEMPRE que se cree un
        # objeto de esta clase se creará con el atributo con dicho valor
        self.edad = 5
        self.peso = 25
        self.clase = "Mamífero"
        self.distancia = 32.5
    
    def saltar(self):
        pass

    def patear(self, objetivo):
        pass