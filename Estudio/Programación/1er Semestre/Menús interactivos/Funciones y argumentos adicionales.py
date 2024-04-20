def mostrar_menu():
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("q. Salir")

def ejecutar_opcion(opcion, argumento):
    if opcion == 1:
        print(f"Has seleccionado la opción 1 con el argumento: {argumento}")
    elif opcion == 2:
        print(f"Has seleccionado la opción 2 con el argumento: {argumento}")
    elif opcion == 3:
        print(f"Has seleccionado la opción 3 con el argumento: {argumento}")
    elif opcion == 'q':
        print("¡Hasta luego!")
    else:
        print("Opción inválida")

def obtener_opcion_valida():
    opciones_validas = [1, 2, 3, 'q']
    while True:
        opcion = input("Selecciona una opción: ")
        if opcion.isdigit() and int(opcion) in opciones_validas:
            return int(opcion)
        elif opcion.lower() in opciones_validas:
            return opcion.lower()
        print("Opción inválida. Inténtalo nuevamente.")

def menu_interactivo():
    while True:
        mostrar_menu()
        opcion = obtener_opcion_valida()
        if opcion == 'q':
            break
        argumento = input("Ingrese un argumento: ")
        ejecutar_opcion(opcion, argumento)