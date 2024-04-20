import math

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

if numero2 != 0:
    division = numero1 / numero2
else:
    division = "No se puede dividir por cero."

if numero1 >= 0:
    raiz_cuadrada = math.sqrt(numero1)
else:
    raiz_cuadrada = "No se puede calcular la raíz de un número negativo."

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("Raíz cuadrada del primer número:", raiz_cuadrada)
