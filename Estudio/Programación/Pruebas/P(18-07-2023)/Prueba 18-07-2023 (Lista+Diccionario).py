s = "s"
n = "n"

print()
Productos = {}
Precios = []
ListaP = [
    Productos
]


switch = True
while switch:
    print("(/°<°)/ -+*|Registro de Ventas MSrLuna|*+- \(°>°\)")
    print()
    print("1. Registrar ventas")
    print("2. Ver ventas")
    print("3. Total de ventas")
    print("4. Salir")
    print()
    try:
        MO = int(input("Ingrese opción númerica: "))
        print()
    except:
        print()
        print("Error, solo valores numericos, no texto \(^_^\).")
        print()
        continue
    if MO == 1:
        Producto = str(input("Nombre del Producto: "))
        try:
            Precio = int(input("Precio del Producto: "))
        except:
            print()
            print("Error, pedí precio, nada de texto \(`_´\).")
            print()
            continue
        Productos[Producto] = Precio
        Precios.append(Precio)
        print()
        continue

    elif MO == 2:
        print("----->",ListaP, "<-----")
        print()
        continue

    elif MO == 3:

        Total = sum(Precios)
        print("$$$", ListaP, "$$$")
        print(f"El total recaudado es un total de ${Total}CLP \(°<°)/.")
        print()
        continue

    elif MO == 4:
        print("Adiós Vuelve pronto... (T^T)")
        print()
        Contador = False

    else:
        print("Opción no válida, pero asumiré que deseas salir (¬_¬), ¡Adiós!")
        print()
        Contador = False
    print()
    print()