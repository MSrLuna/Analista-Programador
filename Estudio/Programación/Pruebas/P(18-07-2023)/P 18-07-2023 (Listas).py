s = "s"
n = "n"

print()
Productos = []
Precios = []
Ventas = [
    Productos,
    Precios
]

switch = True
while switch:
    print("Bienvenido al registro de Ventas MSrLuna")
    print()
    print("1. Registrar ventas")
    print("2. Ver ventas")
    print("3. Total de ventas")
    print("4. Salir")
    print()
    MO = int(input("Ingrese opción númerica: "))
    print()
    if MO == 1:
        Producto = str(input("Nombre del Producto: "))
        Productos.append(Producto)
        Precio = int(input("Precio del Producto: "))
        Precios.append(Precio)

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

    elif MO == 2:
        print(Ventas)
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

    elif MO == 3:

        Total = sum(Precios)
        print(Ventas)
        print(f"El total recaudado es un total de ${Total}CLP.")
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

    elif MO == 4:
        print("Adiós")
        print()
        Contador = False

    else:
        print("Opción no válida, pero asumiré que desea salir, Adiós")
        print()
        Contador = False
    print()
    print()