#Pares
arreglo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sumaPares = 0
for numero in arreglo:
    if numero % 2 == 0:
        sumaPares += numero

print("La suma de los números pares es:", sumaPares)

#----------

#Impares
arreglo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sumaImpares = 0
for numero in arreglo:
    if numero % 2 != 0:  # Cambiamos la condición de divisibilidad por 2 para verificar si es impar
        sumaImpares += numero

print("La suma de los números impares es:", sumaImpares)
