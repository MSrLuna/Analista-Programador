# Realizar un ALGORITMO que permita ingresar los valores necesarios para resolver la ecuación de segundo grado.

import math

# Ingreso de los valores de los coeficientes a, b y c
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

# Cálculo del discriminante
discriminante = b**2 - 4*a*c

# Verificación de solución en números reales
if discriminante < 0:
    print("La ecuación no tiene solución en los números reales")
else:
    # Cálculo de las soluciones
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    
    # Impresión de las soluciones
    print("Las soluciones de la ecuación son:")
    print("x1 =", x1)
    print("x2 =", x2)