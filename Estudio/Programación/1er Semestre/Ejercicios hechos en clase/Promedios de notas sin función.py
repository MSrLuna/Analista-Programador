lista_ramos = []
lista_promedios = []
total_notas = []

ramos = 0
while ramos <= 0 or ramos >= 6:
    ramos = int(input("Ingrese cantidad de ramos a los que sacar promedio (solo existen 5 ramos): "))
    if ramos <= 0 or ramos >= 6:
        print(" ")
        print("Cantidad de ramos inválida. Inténtelo nuevamente.")
        print(" ")
        continue

contador2 = 1
while contador2 <= ramos:
    print(" ")
    print("{}. Ramos disponibles a elegir:".format(contador2))
    print(" ")
    print("[1] Formación Ciudadana.")
    print("[2] Fundamentos de Base de Datos.")
    print("[3] Fundamentos de Hardware y Software.")
    print("[4] Introducción a la Programación.")
    print("[5] Resolución de Problemas de Álgebra.")
    print(" ")
    ramo = int(input("Seleccione ramo: "))
    if ramo == 1:
        ramo_seleccionado = "FC"
    elif ramo == 2:
        ramo_seleccionado = "FBD"
    elif ramo == 3:
        ramo_seleccionado = "FHS"
    elif ramo == 4:
        ramo_seleccionado = "IP"
    elif ramo == 5:
        ramo_seleccionado = "RPÁ"
    else:
        print(" ")
        print("¡¡¡Opción no existente, vuelva a intentarlo!!!")
        continue
    if ramo_seleccionado in lista_ramos:
        print(" ")
        print("¡¡¡El ramo ya ha sido seleccionado, elija otro!!!")
        continue
    lista_ramos.append(ramo_seleccionado)
    print(" ")
    cantidad_notas = int(input("Ingrese cantidad de notas: "))
    print(" ")
    contador = 1
    while contador <= cantidad_notas:
        nota = float(input("{}. Ingrese nota: ".format(contador)))
        total_notas.append(nota)
        contador = contador + 1
    suma_notas = sum(total_notas)
    cantidad_lista = len(total_notas)
    promedio = suma_notas / cantidad_lista
    lista_promedios.append(promedio)
    contador2 = contador2 + 1
print(" ")
print("Ramos y sus promedios en orden:")
print(" ")
print(lista_ramos)
print(lista_promedios)