numero = float(input("Ingrese un número: "))
exponente = int(input("Ingrese el exponente: "))

resultado = 1
for _ in range(exponente):
    resultado *= numero

print("El resultado es:", resultado)
