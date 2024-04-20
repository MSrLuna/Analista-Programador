class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print("Hola, soy", self.nombre)

persona1 = Persona("Ana", 25)
persona1.saludar()

#Las clases se utilizan para definir objetos y sus propiedades.
#El método __init__ es el constructor de la clase y se ejecuta cuando se crea un nuevo objeto.
#Los métodos definidos en una clase pueden usarse para realizar acciones relacionadas con el objeto.