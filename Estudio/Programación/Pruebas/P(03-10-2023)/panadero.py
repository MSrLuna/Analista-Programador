from trabajador import Trabajador



class Panadero(Trabajador):
    def __init__(self):
        super().__init__()
        self.diastrabajados = 10
        self.valordiatrabajo = 15000
        self.antiguedad = 0
        self.años = 0

    def trabajar(self, aprovación):
        if aprovación == 1:
            if self.estadosalud == True:
                self.diastrabajados += 1
                self.antiguedad += 1

                print(f"El Panadero {self.nombre} {self.apellido} ha trabajado un día más (total: {self.diastrabajados} días).")
            else:
                print(f"El Panadero {self.nombre} {self.apellido} no ha trabajado al encontrarse enfermo.")

    def pagarsueldo(self, aprovación):
        if aprovación == 1:

            vdt = self.valordiatrabajo
            dt = self.diastrabajados

            pago = vdt * dt

            self.capital += pago

            print(f"El Panadero {self.nombre} {self.apellido} ha trabajado {self.diastrabajados} y recibe como paga de ${pago}.")

            self.diastrabajados = 0

    def despedir(self, aprovación):
        if aprovación == 1:
            if self.años > 0:
                años = self.antiguedad / 365
                self.años += años
                pago = (self.valordiatrabajo*20)*self.años
                self.capital += pago
                print(f"Pagado ${pago} por los {años} trabajados.")
            else:
                print("Ningún año trabajado, no hay paga.")