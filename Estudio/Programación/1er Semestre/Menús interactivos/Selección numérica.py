def mostrar_menu():
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")

def ejecutar_opcion(opcion):
    if opcion == 1:
        print("Has seleccionado la opción 1")
    elif opcion == 2:
        print("Has seleccionado la opción 2")
    elif opcion == 3:
        print("Has seleccionado la opción 3")
    elif opcion == 4:
        print("¡Hasta luego!")
    else:
        print("Opción inválida")

def menu_interactivo():
    while True:
        mostrar_menu()
        opcion = int(input("Selecciona una opción: "))
        ejecutar_opcion(opcion)
        if opcion == 4:
            break
