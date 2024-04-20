#Crear una clase que contenga 3 objetos a gusto y que se muestren los atributos de cada objeto con print()

class Estudiante:
    def __init__(self, nombre, apellido, rut, edad, semestre):
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut
        self.edad = edad
        self.semestre = semestre

    def mostrar_informacion(self):
        print(f"Alumno: {self.nombre}"+f" {self.apellido}")
        print(f"Rut: {self.rut}")
        print(f"Edad: {self.edad}")
        print(f"Semestre: {self.semestre}")
        print("-" * 20)

# Crear tres objetos de estudiantes
estudiante1 = Estudiante("Juan", "Pérez", "21125033-3", 20, "1er Semestre")
estudiante2 = Estudiante("María", "Antonieta", "20284763-k", 21, "3er Semestre")
estudiante3 = Estudiante("Carlos", "Guanchutripai", "20856235-2", 22, "2do Semestre")

# Mostrar la información de los estudiantes
print("Información de Estudiantes:")
estudiante1.mostrar_informacion()
estudiante2.mostrar_informacion()
estudiante3.mostrar_informacion()
