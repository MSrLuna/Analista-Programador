class Trabajador:
    def __init__(self):
        self.nombre = None
        self.apellido = None
        self.estadosalud = True
        self.capital = 0
    
    def enfermar(self, aprovación):
        if aprovación == 1:
            if self.estadosalud == True:
                self.estadosalud = False

                print(f"El Panadero {self.nombre} {self.apellido} ha enfermado.")
            
            else:

                print(f"El Panadero {self.nombre} {self.apellido} ya está enfermo.")

    def recuperarse(self, aprovación):
        if aprovación == 1:
            if self.estadosalud == False:
                self.estadosalud = True

                print(f"El Panadero {self.nombre} {self.apellido} se ha recuperado.")
            
            else:
                print(f"El Panadero {self.nombre} {self.apellido} no necesita recuperación.")