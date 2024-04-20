import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

def potencia(a, b):
    return math.pow(a, b)

def raiz_cuadrada(a):
    return math.sqrt(a)

print("==== Calculadora Científica ====")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Potencia")
print("6. Raíz Cuadrada")
print("7. Salir")
print("===============================")

while True:
    opcion = input("Selecciona una opción: ")
    if opcion.isdigit() and int(opcion) >= 1 and int(opcion) <= 7:
        opcion = int(opcion)
        break
    print("Opción inválida. Inténtalo nuevamente.")

if opcion == 7:
    print("\n¡Hasta luego!")
elif opcion == 6:
    num = float(input("Ingrese un número: "))
    resultado = raiz_cuadrada(num)
    print(f"\nLa raíz cuadrada de {num} es: {resultado}")
else:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if opcion == 1:
        resultado = suma(num1, num2)
        print(f"\nEl resultado de la suma es: {resultado}")
    elif opcion == 2:
        resultado = resta(num1, num2)
        print(f"\nEl resultado de la resta es: {resultado}")
    elif opcion == 3:
        resultado = multiplicacion(num1, num2)
        print(f"\nEl resultado de la multiplicación es: {resultado}")
    elif opcion == 4:
        resultado = division(num1, num2)
        print(f"\nEl resultado de la división es: {resultado}")
    elif opcion == 5:
        resultado = potencia(num1, num2)
        print(f"\nEl resultado de la potencia es: {resultado}")
