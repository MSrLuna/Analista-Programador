nombre = input("Ingrese nombre del alumno: ")

lista_nombres = []
lista_datos = []
lista_notas = []

n1 = 0
n2 = 0
n3 = 0

contador2 = 1
while contador2 <= 1:
    print(" ")
    print("Opciones disponibles a elegir:")
    print(" ")
    print("[1] Ingresar nota 1.")
    print("[2] Ingresar nota 2.")
    print("[3] Ingresar nota 3.")
    print("[4] Sacar promedio.")
    print(" ")
    opción = int(input("Seleccione opción: "))
    print(" ")
    if opción == 1:
        opción_seleccionada = "n1"
        lista_datos.append(opción_seleccionada)
        n1 = float(input("Ingrese la nota 1: "))
        if n1 < 1 or n1 > 7:
            print("Nota fuera de rango")
            continue
        lista_notas.append(n1)
    elif opción == 2:
        opción_seleccionada = "n2"
        lista_datos.append(opción_seleccionada)
        n2 = float(input("Ingrese la nota 2: "))
        if n2 < 1 or n2 > 7:
            print("Nota fuera de rango")
            continue
        lista_notas.append(n2)
    elif opción == 3:
        opción_seleccionada = "n3"
        lista_datos.append(opción_seleccionada)
        n3 = float(input("Ingrese la nota 3: "))
        if n3 < 1 or n3 > 7:
            print("Nota fuera de rango")
            continue
        lista_notas.append(n3)
    elif opción == 4:
        if n1 >= 1 or n2 >= 1 or n3 >= 1:
            opción_seleccionada = "pr"
            lista_datos.append(opción_seleccionada)
            notas = sum(lista_notas)
            numero_notas = len(lista_notas)
            promedio_final = notas / numero_notas

            print("El promedio de {} es:".format(nombre), promedio_final)

            break
        else:
            print(" ")
            print("¡¡¡No haz ingresado notas a sacar promedio aún!!!")
            continue
    else:
        print(" ")
        print("¡¡¡Opción no existente, vuelva a intentarlo!!!")
        continue
    if opción in lista_datos:
        print(" ")
        print("¡¡¡Esa opción ya ha sido seleccionada, elija otra!!!")
        continue