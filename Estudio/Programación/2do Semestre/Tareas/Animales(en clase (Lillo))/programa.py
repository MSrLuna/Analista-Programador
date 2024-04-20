from canguro import Canguro
from delfin import Delfin
'''
c = Canguro()
c.avanzar(10)
# SIEMPRE que un método RETORNA un valor lo DEBES guardar en una variable
# Crea una variable y dale como valor la llamada al método
datos = c.mostrarDatos()
print(datos)
'''
opcion = int(input("Bienvenido.. para continuar pulse 1, si desea salir pulse 0"))
while (opcion != 0):
    print("Elija un animal: ")
    print("1. Canguro")
    print("2. Delfín")
    print("0. Salir")
    opAnimal = int(input())

    if (opAnimal == 1):
        # al construir un objeto en realidad LLAMAMOS AL CONSTRUCTOR __init__()
        c = Canguro()
        print("Elija una acción que quiera que se realice:")
        print("1. Avanzar")
        print("2. Comer")
        opAccion = int(input())

        if opAccion == 1:
            asdf = int(input("Ingrese la cantidad de kms. que va a recorrer: "))
            c.avanzar(asdf)
            datos = c.mostrarDatos()
            print(datos)

    elif (opAnimal == 2):
        print("Elija una acción que quiera que se realice:")
        print("1. Avanzar")
        print("2. Comer")
    elif (opAnimal == 0):
        break

print("FIN DEL PROGRAMA")