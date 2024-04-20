import math
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
suma = num1 + num2
print("La suma es:", suma)
resta = num1 - num2
print("La resta es:", resta)
multiplicacion = num1 * num2
print("La multiplicación es:", multiplicacion)
if num2 != 0:
	division = num1 / num2
	print("La división es:", division)
else:
	print("No se puede dividir por 0")
if num1 >= 0:
	raiz_cuadrada = math.sqrt(num1)
	print("La raíz cuadrada del primer número es:", raiz_cuadrada)
else:
    print("No se puede sacar la raíz cuadrada de un número negativo")