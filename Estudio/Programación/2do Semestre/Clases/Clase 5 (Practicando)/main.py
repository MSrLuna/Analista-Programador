from producto import Producto

def menu_acciones():
    print("Seleccione una acción: ")
    print()
    print("1. Consultar datos.")
    print("2. Insertar registros.")
    print("3. Actualizar un registro.")
    print("4. Eliminar un registro.")
    print()
print("Bienvenido al programa para administrar productos.")
print()
while (True):
    print("Seleccione una de las siguientes opciones:")
    print()
    print("1. Administrar productos.")
    print("2. Administrar tipos de productos.")
    print("0. Salir.")
    print()
    opcion = int(input("--> "))
    print()
    if opcion == 1:
        p = Producto()
        menu_acciones()
        accion_seleccionada = int(input())
        print()
        if accion_seleccionada == 1:
            #Acá tenemos que hacer un SELECT a la tabla PRODUCTO.
            p.Obtener_todos()
            pass
        elif accion_seleccionada == 2:
            #Hacer un INSERT a la tabla PRODUCTO.
            p.nombre = input("Nombre producto: ")
            p.precio = int(input("Precio producto: "))
            p.stock = int(input("Stock producto: "))
            p.Insertar()
            pass
        elif accion_seleccionada == 3:
            #Hacer un UPDATE a la tabla PRODUCTO.
            p.Obtener_todos()
            pass
        elif accion_seleccionada == 4:
            #Hacer un DELETE a la tabla PRODUCTO.
            p.Obtener_todos()
            pass
    elif opcion == 2:
        menu_acciones()
    elif opcion == 0:
        break
print("Fin del programa.")
print()