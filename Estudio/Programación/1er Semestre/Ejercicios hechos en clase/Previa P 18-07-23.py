# Administrador de tareas:
s = "s"
n = "n"

Lista_Tareas = []
Contador = True
while Contador:
    print()
    print("Bienvenido al Administrador de tareas, seleccione la acción deseada:")
    print()
    print("1. Ver todas las tareas.")
    print("2. Agregar tarea.")
    print("3. Completar tarea.")
    print("Otro. Salir.")
    print()
    Opción = int(input("Valor númerico: "))
    print()
    if Opción == 1:
        print(Lista_Tareas)
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

    elif Opción == 2:
        N_tarea = str(input("Ingrese la tarea: "))
        Lista_Tareas.append(N_tarea)
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
    elif Opción == 3:
        print(Lista_Tareas)
        print()
        N_T_eliminar = str(input("Ingrese la tarea: "))
        print()
        if N_T_eliminar in Lista_Tareas:
            Lista_Tareas.remove(N_T_eliminar)
            print(f"Se ha completado la tarea: {N_T_eliminar} con éxito.")
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
        else:
            print(f"No existe la tarea: {N_T_eliminar}.")
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
    else:
        print("Adiós")
        print()
        Contador = False