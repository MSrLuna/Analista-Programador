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

def obtener_opcion_valida():
    while True:
        opcion = input("Selecciona una opción: ")
        if opcion.isdigit():
            opcion = int(opcion)
            if opcion >= 1 and opcion <= 4:
                return opcion
        print("Opción inválida. Inténtalo nuevamente.")

def menu_interactivo():
    while True:
        mostrar_menu()
        opcion = obtener_opcion_valida()
        ejecutar_opcion(opcion)
        if opcion == 4:
            break
