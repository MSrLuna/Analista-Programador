def mostrar_menu():
    print("a. Opción A")
    print("b. Opción B")
    print("c. Opción C")
    print("q. Salir")

def ejecutar_opcion(opcion):
    if opcion == 'a':
        print("Has seleccionado la opción A")
    elif opcion == 'b':
        print("Has seleccionado la opción B")
    elif opcion == 'c':
        print("Has seleccionado la opción C")
    elif opcion == 'q':
        print("¡Hasta luego!")
    else:
        print("Opción inválida")

def obtener_opcion_valida():
    opciones_validas = ['a', 'b', 'c', 'q']
    while True:
        opcion = input("Selecciona una opción: ")
        if opcion.lower() in opciones_validas:
            return opcion.lower()
        print("Opción inválida. Inténtalo nuevamente.")

def menu_interactivo():
    while True:
        mostrar_menu()
        opcion = obtener_opcion_valida()
        ejecutar_opcion(opcion)
        if opcion == 'q':
            break
