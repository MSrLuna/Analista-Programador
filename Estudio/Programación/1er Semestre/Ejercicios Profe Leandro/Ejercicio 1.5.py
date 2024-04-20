# Este programa permite al usuario ingresar números enteros hasta que ingrese un número no positivo.

while True:
    num = int(input("Ingresa un número entero: "))  # Se solicita al usuario que ingrese un número entero
    if num > 0:  # Si el número es mayor que 0, es positivo
        print("Positivo")  # Se muestra un mensaje que dice "Positivo"
        print(num)  # Se muestra el número por pantalla
    else:
        break  # Si el número no es positivo, se sale del ciclo while