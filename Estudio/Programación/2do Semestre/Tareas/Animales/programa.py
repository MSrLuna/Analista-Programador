from animal import Animal
from canguro import Canguro
from cocodrilo import Cocodrilo
from pollo import Pollo
from delfín import Delfín

a = Cocodrilo()
b = Canguro()
c = Delfín()
d = Pollo()

contador_menu = True
while contador_menu:
    try:
        print()
        print("Bienvenido, confirme para continuar...")
        print()
        opcion_menu_continuar = str(input("( S / N ): "))
        print()
        if opcion_menu_continuar == "s" or opcion_menu_continuar == "S":
            print("Elija un animal:")
            print()
            print("1. Cocodrilo.")
            print("2. Canguro.")
            print("3. Delfín.")
            print("4. Pollo.")
            print("otro. Salir")
            print()
            opcion_animal = int(input("( 1 / 2 / 3 / 4 ): "))
            print()
            if opcion_animal == 1:
                print("Datos Cocodrilo:")
                print()
                print(f"Nombre:    | {a.nombre}")
                print(f"Raza:      | {a.raza}")
                print(f"Edad:      | {a.edad}")
                print(f"Peso:      | {a.peso}")
                print(f"Clase:     | {a.clase}")
                print(f"Distancia: | {a.distancia}")
                print()
                print("Seleccione acción:")
                print()
                print("1. Comer.")
                print("2. Avanzar.")
                print()
                opcion_accion_animal = int(input("( 1 / 2 ): "))
                print()
                if opcion_accion_animal == 1:
                    print("Ingrese kgs a consumir por el animal:")
                    print()
                    kilogramos = float(input("--> "))
                    print()
                    a.comer(kilogramos)
                    print("¿Volver a intentar?")
                    print()
                    print("1. Sí")
                    print("2. No")
                    print()
                    opcion_reintento = int(input("( 1 / 2 ): "))
                    print()
                    if opcion_reintento == 1:
                        print("Entendido.")
                        continue
                    elif opcion_reintento == 2:
                        print("Entendido, vuelve pronto...")
                        contador_menu = False
                elif opcion_accion_animal == 2:
                    print("Ingrese kms a recorrer por el animal:")
                    print()
                    kilometros = float(input("--> "))
                    print()
                    a.avanzar(kilometros)
                    print("¿Volver a intentar?")
                    print()
                    print("1. Sí")
                    print("2. No")
                    print()
                    opcion_reintento = int(input("( 1 / 2 ): "))
                    print()
                    if opcion_reintento == 1:
                        print("Entendido.")
                        continue
                    elif opcion_reintento == 2:
                        print("Entendido, vuelve pronto...")
                        contador_menu = False
            elif opcion_animal == 2:
                print("Datos Canguro:")
                print()
                print(f"Nombre:    | {b.nombre}")
                print(f"Raza:      | {b.raza}")
                print(f"Edad:      | {b.edad}")
                print(f"Peso:      | {b.peso}")
                print(f"Clase:     | {b.clase}")
                print(f"Distancia: | {b.distancia}")
                print()
                print("Seleccione acción:")
                print()
                print("1. Comer.")
                print("2. Avanzar.")
                print()
                opcion_accion_animal = int(input("( 1 / 2 ): "))
                print()
                if opcion_accion_animal == 1:
                    print("Ingrese kgs a consumir por el animal:")
                    print()
                    kilogramos = float(input("--> "))
                    print()
                    b.comer(kilogramos)
                    print("¿Volver a intentar?")
                    print()
                    print("1. Sí")
                    print("2. No")
                    print()
                    opcion_reintento = int(input("( 1 / 2 ): "))
                    print()
                    if opcion_reintento == 1:
                        print("Entendido.")
                        continue
                    elif opcion_reintento == 2:
                        print("Entendido, vuelve pronto...")
                        contador_menu = False
                elif opcion_accion_animal == 2:
                    print("Ingrese kms a recorrer por el animal:")
                    print()
                    kilometros = float(input("--> "))
                    print()
                    b.avanzar(kilometros)
                    print("¿Volver a intentar?")
                    print()
                    print("1. Sí")
                    print("2. No")
                    print()
                    opcion_reintento = int(input("( 1 / 2 ): "))
                    print()
                    if opcion_reintento == 1:
                        print("Entendido.")
                        continue
                    elif opcion_reintento == 2:
                        print("Entendido, vuelve pronto...")
                        contador_menu = False
            elif opcion_animal == 3:
                print("Datos Delfín:")
                print()
                print(f"Nombre:    | {c.nombre}")
                print(f"Raza:      | {c.raza}")
                print(f"Edad:      | {c.edad}")
                print(f"Peso:      | {c.peso}")
                print(f"Clase:     | {c.clase}")
                print(f"Distancia: | {c.distancia}")
                print()
                print("Seleccione acción:")
                print()
                print("1. Comer.")
                print("2. Avanzar.")
                print()
                opcion_accion_animal = int(input("( 1 / 2 ): "))
                print()
                if opcion_accion_animal == 1:
                    print("Ingrese kgs a consumir por el animal:")
                    print()
                    kilogramos = float(input("--> "))
                    print()
                    c.comer(kilogramos)
                    print("¿Volver a intentar?")
                    print()
                    print("1. Sí")
                    print("2. No")
                    print()
                    opcion_reintento = int(input("( 1 / 2 ): "))
                    print()
                    if opcion_reintento == 1:
                        print("Entendido.")
                        continue
                    elif opcion_reintento == 2:
                        print("Entendido, vuelve pronto...")
                        contador_menu = False
                elif opcion_accion_animal == 2:
                    print("Ingrese kms a recorrer por el animal:")
                    print()
                    kilometros = float(input("--> "))
                    print()
                    c.avanzar(kilometros)
                    print("¿Volver a intentar?")
                    print()
                    print("1. Sí")
                    print("2. No")
                    print()
                    opcion_reintento = int(input("( 1 / 2 ): "))
                    print()
                    if opcion_reintento == 1:
                        print("Entendido.")
                        continue
                    elif opcion_reintento == 2:
                        print("Entendido, vuelve pronto...")
                        contador_menu = False
            elif opcion_animal == 4:
                print("Datos Pollo:")
                print()
                print(f"Nombre:    | {d.nombre}")
                print(f"Raza:      | {d.raza}")
                print(f"Edad:      | {d.edad}")
                print(f"Peso:      | {d.peso}")
                print(f"Clase:     | {d.clase}")
                print(f"Distancia: | {d.distancia}")
                print()
                print("Seleccione acción:")
                print()
                print("1. Comer.")
                print("2. Avanzar.")
                print()
                opcion_accion_animal = int(input("( 1 / 2 ): "))
                print()
                if opcion_accion_animal == 1:
                    print("Ingrese kgs a consumir por el animal:")
                    print()
                    kilogramos = float(input("--> "))
                    print()
                    d.comer(kilogramos)
                    print("¿Volver a intentar?")
                    print()
                    print("1. Sí")
                    print("2. No")
                    print()
                    opcion_reintento = int(input("( 1 / 2 ): "))
                    print()
                    if opcion_reintento == 1:
                        print("Entendido.")
                        continue
                    elif opcion_reintento == 2:
                        print("Entendido, vuelve pronto...")
                        contador_menu = False
                elif opcion_accion_animal == 2:
                    print("Ingrese kms a recorrer por el animal:")
                    print()
                    kilometros = float(input("--> "))
                    print()
                    d.avanzar(kilometros)
                    print("¿Volver a intentar?")
                    print()
                    print("1. Sí")
                    print("2. No")
                    print()
                    opcion_reintento = int(input("( 1 / 2 ): "))
                    print()
                    if opcion_reintento == 1:
                        print("Entendido.")
                        continue
                    elif opcion_reintento == 2:
                        print("Entendido, vuelve pronto...")
                        contador_menu = False
            else:
                print("Entendido, vuelve pronto...")
                contador_menu = False
        elif opcion_menu_continuar == "n" or opcion_menu_continuar == "N":
            print("Entendido, vuelve pronto...")
            contador_menu = False
        else:
            print("Opción no valida, vuelve a intentarlo.")
            print()
            print("Presione cualquier cosa para continuar.")
            print()
            nada = input()
            continue
    except:
        print("Error al ingresar dato.")
        print()
        print("Presione cualquier cosa para continuar.")
        print()
        nada = input()