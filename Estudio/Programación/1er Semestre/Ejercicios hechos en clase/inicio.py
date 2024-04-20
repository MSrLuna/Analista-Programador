def saludarpersona(nombre):
    print("Hola", nombre)
nom = input("Ingrese nombre: ")
saludarpersona(nom)

def positivonegativo(numero):
    if numero > 0:
        print("Positivo")
    elif numero == 0:
        print("Neutro")
    else:
        print("Negativo")

num = int(input("N°: "))
positivonegativo(num)