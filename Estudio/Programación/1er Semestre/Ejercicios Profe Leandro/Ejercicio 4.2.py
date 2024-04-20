#Crear un D.F. que permita sacar el factorial de un número ingresado por
#teclado y mostrar su resultado por pantalla. Ejemplos de factoriales:
#Factorial de 3 >> 1*2*3 = 6
#Factorial de 5 >> 1*2*3*4*5 = 120
#Factorial de 6 >> 1*2*3*4*5*6 = 720

numero = int(input("Ingrese un número para calcular su factorial: "))
factorial = 1

for i in range(1, numero + 1):
    factorial *= i

print("El factorial de", numero, "es:", factorial)