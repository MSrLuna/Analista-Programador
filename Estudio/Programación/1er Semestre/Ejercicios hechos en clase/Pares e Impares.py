numero = int(input("Ingrese un número: "))

pares = []
impares = []

# Recorremos todos los números desde 1 hasta el número ingresado
for i in range(1, numero + 1):
    if i % 2 == 0:
        pares.append(i)  # Si es par, lo agregamos a la lista de pares
    else:
        impares.append(i)  # Si es impar, lo agregamos a la lista de impares

print("Números pares:", pares)
print("Números impares:", impares)
