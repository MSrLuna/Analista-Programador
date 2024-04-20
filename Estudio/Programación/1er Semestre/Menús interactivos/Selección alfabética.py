def mostrar_menu():
    print("Menú:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("q. Salir")

def ejecutar_opcion(opcion):
    opciones = {
        '1': opcion_1,
        '2': opcion_2,
        '3': opcion_3,
        'q': opcion_salir
    }
    if opcion in opciones:
        opciones[opcion]()
    else:
        print("Opción inválida")

def opcion_1():
    print("Has seleccionado la opción 1")

def opcion_2():
    print("Has seleccionado la opción 2")

def opcion_3():
    print("Has seleccionado la opción 3")

def opcion_salir():
    print("¡Hasta luego!")

def menu_interactivo():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        ejecutar_opcion(opcion.lower())
        if opcion == 'q':
            break
