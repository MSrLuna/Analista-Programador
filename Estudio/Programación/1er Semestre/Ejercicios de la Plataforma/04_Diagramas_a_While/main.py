# PRIMER PASO para solucionar el ejercicio.. definir que el WHILE dure 3 ciclos
contador = 1
totalNotas = 0
while contador <= 3:
    # FALTA TODAVÍA validar que las notas ingresadas estén dentro del rango académico
    nota = float(input("Ingrese nota " + str(contador) + ": "))
    if nota >= 1 and nota <= 7:
        totalNotas = totalNotas + nota
        contador = contador + 1
    else:
        #En el caso del else, no sumo el contador.. así se mantiene el while en el
        # mismo bucle, hasta que se ingrese un valor correcto
        print("soy entero lagi loko.. ingresa de nuevo la nota ziii")
        # break rompe el ciclo actual
        #break

promedio = totalNotas / 3
print(promedio)

if True:
    print("Estoy DENTRO del IF")
print("Estoy FUERA del IF")