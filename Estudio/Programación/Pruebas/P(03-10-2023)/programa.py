from trabajador import Trabajador
from panadero import Panadero

p = Panadero()
llamada=1

try:
    print("Prueba 1.2 de Programación")
    print("Ingrese la siguiente información para crear un trabajador Panadero: ")
    print()
    p.nombre = str(input("Nombre: "))
    p.apellido = str(input("Apellido: "))
    print()
    print("¿Desea modificar más datos? (datos por defecto en caso de negarse).")
    print()
    opcion_inicio = str(input("s/n: "))
    print()
    if opcion_inicio == "s" or opcion_inicio == "S":
        p.capital = int(input("Ingrese capital inicial: "))
        p.diastrabajados = int(input("Días trabajados del mes: "))
        p.valordiatrabajo = int(input("Valor día de trabajo: "))
        p.antiguedad = int(input("Años trabajando: "))
        print()
    else:
        pass
    p.antiguedad += p.diastrabajados
    # realizar código para crear un Panadero según los datos ingresados por teclado..

except:

    print("-Error 1- opción ingresada incorrecta. Intente nuevamente.")
    print()

try:

    switch_menu = True
    while switch_menu:
        print("Seleccione una opción: ")
        print()

        print("1. Enfermar al Trabajador.")
        print("2. Recuperar saludud del Trabajador.")
        print("3. Trabajar.")
        print("4. Pagar sueldo.")
        print("5. Despedir.")
        print("6. Mostrar Datos.")
        print("0. Salir.")
        print()

        opcion = int(input("--> "))
        print()
        try:

            if opcion == 1:
                p.enfermar(llamada)
                print()
            elif opcion == 2:
                p.recuperarse(llamada)
                print()
            elif opcion == 3:
                p.trabajar(llamada)
                print()
            elif opcion == 4:
                p.pagarsueldo(llamada)
                print()
            elif opcion == 5:
                p.despedir(llamada)
                switch_menu = False
                print()
            elif opcion == 6:
                print(f"Nombre: {p.nombre}")
                print(f"Apellido: {p.apellido}")
                print(f"Estado de salud: {p.estadosalud}")
                print(f"Capital: {p.capital}")
                print(f"Días trabajados: {p.diastrabajados}")
                print(f"Valor día de trabajo: {p.valordiatrabajo}")
                print(f"Años trabajando: {p.años}")
                print()
            elif opcion == 0:
                print("Fin del programa.")
                print()
                switch_menu = False
            else:
                print("Opción ingresada incorrecta. Intente nuevamente.")
                print()
        except:

            print("-Error 3- opción ingresada incorrecta. Intente nuevamente.")
            print()

except:

    print("-Error 2- opción ingresada incorrecta. Intente nuevamente.")
    print()