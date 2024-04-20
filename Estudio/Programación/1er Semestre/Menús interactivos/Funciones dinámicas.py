def mostrar_menu():
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Salir")

def sumar():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 + num2
    print(f"El resultado de la suma es: {resultado}")

def restar():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 - num2
    print(f"El resultado de la resta es: {resultado}")

def multiplicar():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 * num2
    print(f"El resultado de la multiplicación es: {resultado}")

def menu_interactivo():
    while True:
        mostrar_menu()
        opcion = int(input("Selecciona una opción: "))
        if opcion == 1:
            sumar()
        elif opcion == 2:
            restar()
        elif opcion == 3:
            multiplicar()
        elif opcion == 4:
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida")

