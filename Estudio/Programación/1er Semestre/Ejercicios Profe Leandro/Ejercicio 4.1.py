#Crear un D.F. que permita ingresar 30 nros. Menores a 100, después mostrar el promedio en pantalla. (use mientras)

contador = 0
acumulador = 0

while contador < 30:
    numero = int(input("Ingrese un número menor a 100: "))
    if numero < 100:
        acumulador += numero
        contador += 1

promedio = acumulador / 30
print("El promedio es:", promedio)