def mostrar_menu():
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("q. Salir")

def ejecutar_opcion(opcion):
    if opcion == 1:
        print("Has seleccionado la opción 1")
    elif opcion == 2:
        print("Has seleccionado la opción 2")
    elif opcion == 3:
        print("Has seleccionado la opción 3")
    elif opcion == 'q':
        print("¡Hasta luego!")
    else:
        print("Opción inválida")

def obtener_opcion_valida():
    intentos = 3
    while intentos > 0:
        opcion = input("Selecciona una opción: ")
        if opcion.isdigit() and int(opcion) >= 1 and int(opcion) <= 3:
            return int(opcion)
        elif opcion == 'q':
            return opcion
        else:
            intentos -= 1
            print(f"Opción inválida. Inténtalo nuevamente. Te quedan {intentos} intentos.")
    print("Demasiados intentos fallidos. Saliendo...")
    return 'q'

def menu_interactivo():
    while True:
        mostrar_menu()
        opcion = obtener_opcion_valida()
        ejecutar_opcion(opcion)
        if opcion == 'q':
            break
