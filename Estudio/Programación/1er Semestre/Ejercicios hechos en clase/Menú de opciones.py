def resultado_ejercicio(R):
    print(" ")
    print("El resultado en su...", lista_ejercicios)
    print(" ")
    print("      es", resultado)
    print(" ")
    print("     \(^~^)/")

print(" ")
print(" / / / ¡¡Welcome to MSr.Luna Calculator!! \ \ \ ")
print(" ")
print("             Select the exercise.")
print(" ")

contador = True
while contador:
    print("~[1] Sumar~")
    print("~[2] Restar~")
    print("~[3] Multiplicar~")
    print("~[4] Dividir~")
    print(" ")
    ejercicio = int(input("~Seleccione Ejercicio (^o^): "))
    print(" ")

    lista_ejercicios = []

    if ejercicio == 1:
        ejercicio_seleccionado = "Suma"
        lista_ejercicios.append(ejercicio_seleccionado)
        ejercicio_seleccionado1 = int(input("°[Primer número]°  "))
        ejercicio_seleccionado2 = int(input("°[Segundo número]° "))
        resultado = ejercicio_seleccionado1 + ejercicio_seleccionado2
        resultado_ejercicio(resultado)
        contador = False

    elif ejercicio == 2:
        ejercicio_seleccionado = "Resta"
        lista_ejercicios.append(ejercicio_seleccionado)
        ejercicio_seleccionado1 = int(input("°[Primer número]°  "))
        ejercicio_seleccionado2 = int(input("°[Segundo número]° "))
        resultado = ejercicio_seleccionado1 - ejercicio_seleccionado2
        resultado_ejercicio(resultado)
        contador = False

    elif ejercicio == 3:
        ejercicio_seleccionado = "Multiplicación"
        lista_ejercicios.append(ejercicio_seleccionado)
        ejercicio_seleccionado1 = int(input("°[Primer número]°  "))
        ejercicio_seleccionado2 = int(input("°[Segundo número]° "))
        resultado = ejercicio_seleccionado1 * ejercicio_seleccionado2
        resultado_ejercicio(resultado)
        contador = False

    elif ejercicio == 4:
        ejercicio_seleccionado = "División"
        lista_ejercicios.append(ejercicio_seleccionado)
        ejercicio_seleccionado1 = int(input("°[Primer número]°  "))
        ejercicio_seleccionado2 = int(input("°[Segundo número]° "))
        resultado_ejercicio(resultado)
        contador = False

        if ejercicio == 0:
           print(" ")
           print("¡¡¡No puedes dividir por 0!!!")
           continue 
        else:
            resultado = ejercicio_seleccionado1 / ejercicio_seleccionado2

    else:
        print(" ")
        print("¡¡¡Opción no existente, vuelva a intentarlo!!!")
        continue