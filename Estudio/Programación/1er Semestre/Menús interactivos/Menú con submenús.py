def mostrar_menu_principal():
    print("1. Opciones de usuario")
    print("2. Opciones de administrador")
    print("3. Salir")

def mostrar_menu_usuario():
    print("Menú de usuario:")
    print("a. Ver perfil")
    print("b. Modificar contraseña")
    print("c. Volver al menú principal")

def mostrar_menu_administrador():
    print("Menú de administrador:")
    print("a. Agregar usuario")
    print("b. Eliminar usuario")
    print("c. Volver al menú principal")

def ejecutar_opcion_principal(opcion):
    if opcion == 1:
        menu_usuario()
    elif opcion == 2:
        menu_administrador()
    elif opcion == 3:
        print("¡Hasta luego!")

def ejecutar_opcion_usuario(opcion):
    if opcion == 'a':
        print("Mostrando perfil de usuario...")
    elif opcion == 'b':
        print("Modificando contraseña...")
    elif opcion == 'c':
        return

def ejecutar_opcion_administrador(opcion):
    if opcion == 'a':
        print("Agregando usuario...")
    elif opcion == 'b':
        print("Eliminando usuario...")
    elif opcion == 'c':
        return

def obtener_opcion_valida(opciones_validas):
    while True:
        opcion = input("Selecciona una opción: ")
        if opcion.lower() in opciones_validas:
            return opcion.lower()
        print("Opción inválida. Inténtalo nuevamente.")

def menu_usuario():
    while True:
        mostrar_menu_usuario()
        opcion = obtener_opcion_valida(['a', 'b', 'c'])
        ejecutar_opcion_usuario(opcion)
        if opcion == 'c':
            break

def menu_administrador():
    while True:
        mostrar_menu_administrador()
        opcion = obtener_opcion_valida(['a', 'b', 'c'])
        ejecutar_opcion_administrador(opcion)
        if opcion == 'c':
            break

def menu_interactivo():
    while True:
        mostrar_menu_principal()
        opcion = obtener_opcion_valida([1, 2, 3])
        ejecutar_opcion_principal(opcion)
        if opcion == 3:
            break
