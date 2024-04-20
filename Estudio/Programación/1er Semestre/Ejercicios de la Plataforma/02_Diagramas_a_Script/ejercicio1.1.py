# input SIEMPRE ASUME que lo ingresado es un TEXTO
num1 = input("Ingrese número 1: ")
num2 = input("Ingrese número 2: ")
num3 = input("Ingrese número 3: ")
num4 = input("Ingrese número 4: ")
num5 = input("Ingrese número 5: ")

# Para sumar estos valores, necesitamos TRANSFORMARLOS a tipo int
# Se deben transformar a número todos los valores, sino dara ERROR
resultado = int(num1) + int(num2) + int(num3) + int(num4) + int(num5)
print(resultado)