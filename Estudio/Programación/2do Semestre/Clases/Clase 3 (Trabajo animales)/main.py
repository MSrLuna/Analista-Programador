from animal import Animal
from canguro import Canguro
from delfin import Delfin


c = Canguro()
d = Delfin()

# c.nombre = "Tayson"
# c.edad = 5

# d.nombre = "Neptuno"
# d.edad = 4

# print()
# print(f"El canguro {c.nombre} tiene {c.edad} años.")
# print()
# print(f"El delfín {d.nombre} tiene {d.edad} años.")
# print()

# c1 = Canguro()
# c2 = Canguro()
# c3 = Canguro()

# print(f"{c1.edad}, {c2.edad}, {c3.edad}")
# print()

contador = True
while contador:
    print("Elija un animal...")
    print()
    print("1. Canguro.")
    print("2. Delfín.")
    print("otro. salir.")
    print()
    try:
        opanimal = int(input("--> "))
        if opanimal == 1 or opanimal == 2:
            print()
            print("Elija accion a realizar...")
            print()
            print("1. Avanzar.")
            print("2. Comer.")
            print("otro. Cambiar animal")
            print()
            opaccion = int(input("--> "))
            print()
            if opaccion == 1:
                print("Ingrese kms recorridos...")
                print()
                kms = int(input("--> "))
                print()
                if opanimal == 1:
                    c.avanzar(kms)
                else:
                    d.avanzar(kms)
            elif opaccion == 2:
                print("Ingrese kgs consumidos...")
                print()
                kgs = int(input("--> "))
                print()
                if opanimal == 1:
                    c.comer(kgs)
                else:
                    d.comer(kgs)
            else:
                continue
        else:
            contador = False
    except:
        print("Error, solo números")
        continue
