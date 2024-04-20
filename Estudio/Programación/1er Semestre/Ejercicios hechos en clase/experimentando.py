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
    print("Otro número. Salir.")
    print()
    Opción = int(input("Opción: "))
    print()
    if Opción == 1:
        print(Diccionario)
        print()
        op = int(input("¿Desea continuar? 1/otro: "))
        if op == 1:
            continue
        else:
            Contador = False
    elif Opción == 2:
        Buscador = str(input("Palabra que desea buscar: "))
        if Buscador in Diccionario:
            print()
            print("Resultado:")
            print(Diccionario[Buscador])
            print()
            op = int(input("¿Desea continuar? 1/otro: "))
            if op == 1:
                continue
            else:
                Contador = False
        else:
            print()
            print(f"No se ha podido encontrar {Buscador} ya que no se encuentra en el Diccionario.")
            print()
            op = int(input("¿Desea continuar? 1/otro: "))
            if op == 1:
                continue
            else:
                Contador = False
    elif Opción == 3:
        Palabra = str(input("Ingrese palabra a definir: "))
        Definición = str(input("Ingrese definición de la palabra agregada: "))
        Diccionario[Palabra] = Definición
        print()
        op = int(input("¿Desea continuar? 1/otro: "))
        if op == 1:
            continue
        else:
            Contador = False
    elif Opción == 4:
        print(Diccionario)
        print()
        Palabra = str(input("Ingrese palabra a eliminar: "))
        print()
        if Palabra in Diccionario:
            del Diccionario[Palabra]
            print(f"Se ha eliminado {Palabra} y su definición con éxito.")
            print()
            op = int(input("¿Desea continuar? 1/otro: "))
            if op == 1:
                continue
            else:
                Contador = False
        else:
            print(f"No se ha podido eliminar {Palabra} ya que no se encuentra en el Diccionario.")
            print()
            op = int(input("¿Desea continuar? 1/otro: "))
            if op == 1:
                continue
            else:
                Contador = False
    else:
        print("Adiós")
        print()
        Contador = False