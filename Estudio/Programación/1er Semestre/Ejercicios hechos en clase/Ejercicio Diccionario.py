# Simulación de Diccionario.
s = "s"
n = "n"

Diccionario = {}
Contador = True
while Contador:
    print()
    print("Ingrese opción númerica de su siguiente acción deseada:")
    print()
    print("1. Ver contenido del Diccionario hasta el momento.")
    print("2. Buscar Definición de alguna palabra.")
    print("3. Agregar Palabra y Definición.")
    print("4. Eliminar Palabra y Definición.")
    print("Otro. Salir.")
    print()
    Opción = int(input("Opción: "))
    print()
    if Opción == 1:
        print(Diccionario)
        print()
        op = str(input("¿Desea continuar? s/n: "))
        op.lower
        if op == s:
            continue
        elif op == n:
            print()
            print("Adiós")
            print()
            Contador = False
        else:
            print("Opción no válida")
            break

    elif Opción == 2:
        Buscador = str(input("Palabra que desea buscar: "))
        if Buscador in Diccionario:
            print()
            print("Resultado:")
            print(Diccionario[Buscador])
            print()
            op = str(input("¿Desea continuar? s/n: "))
            op.lower
            if op == s:
                continue
            elif op == n:
                print()
                print("Adiós")
                print()
                Contador = False
            else:
                print("Opción no válida")
                break
        else:
            print()
            print(f"No se ha podido encontrar {Buscador} ya que no se encuentra en el Diccionario.")
            print()
            op = str(input("¿Desea continuar? s/n: "))
            op.lower
            if op == s:
                continue
            elif op == n:
                print()
                print("Adiós")
                print()
                Contador = False
            else:
                print("Opción no válida")
                break
    elif Opción == 3:
        Palabra = str(input("Ingrese palabra a definir: "))
        Definición = str(input("Ingrese definición de la palabra agregada: "))
        Diccionario[Palabra] = Definición
        print()
        op = str(input("¿Desea continuar? s/n: "))
        if op == s:
            continue
        elif op == n:
            print()
            print("Adiós")
            print()
            Contador = False
        else:
            print("Opción no válida")
            break
    elif Opción == 4:
        print(Diccionario)
        print()
        Palabra = str(input("Ingrese palabra a eliminar: "))
        print()
        if Palabra in Diccionario:
            del Diccionario[Palabra]
            print(f"Se ha eliminado {Palabra} y su definición con éxito.")
            print()
            op = str(input("¿Desea continuar? s/n: "))
            if op == s:
                continue
            elif op == n:
                print()
                print("Adiós")
                print()
                Contador = False
            else:
                print("Opción no válida")
                break
        else:
            print(f"No se ha podido eliminar {Palabra} ya que no se encuentra en el Diccionario.")
            print()
            op = str(input("¿Desea continuar? s/n: "))
            if op == s:
                continue
            elif op == n:
                print()
                print("Adiós")
                print()
                Contador = False
            else:
                print("Opción no válida")
                break
    else:
        print("Adiós")
        print()
        Contador = False