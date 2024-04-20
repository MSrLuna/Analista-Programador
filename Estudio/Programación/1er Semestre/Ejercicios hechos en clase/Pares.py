numero = int(input("Ingrese un número: "))

print("Números pares hasta", numero, ":")

# Recorremos todos los números desde 1 hasta el número ingresado
for i in range(1, numero + 1):
    if i % 2 == 0:
        print(i)
