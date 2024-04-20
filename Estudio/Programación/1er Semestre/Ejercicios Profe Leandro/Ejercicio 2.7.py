#Crear un ALGORITMO que ingrese 2 números cualquiera, mostrar en pantalla; su suma, resta, multiplicación, división y la raíz cuadrada del primer número. Validar el ingreso para ciertas operaciones, para evitar un error en tiempo de ejecución. No debe dividir por 0, tampoco sacar la raíz de un n° negativo.

import math

# Ingreso de los dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Suma
suma = num1 + num2
print("La suma es:", suma)

# Resta
resta = num1 - num2
print("La resta es:", resta)

# Multiplicación
multiplicacion = num1 * num2
print("La multiplicación es:", multiplicacion)

# División (se valida que num2 sea distinto de 0)
if num2 != 0:
    division = num1 / num2
    print("La división es:", division)
else:
    print("No se puede dividir por 0")

# Raíz cuadrada (se valida que num1 sea positivo o 0)
if num1 >= 0:
    raiz_cuadrada = math.sqrt(num1)
    print("La raíz cuadrada del primer número es:", raiz_cuadrada)
else:
    print("No se puede sacar la raíz cuadrada de un número negativo")