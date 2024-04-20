total_recaudado = 0

n = int(input("Ingrese el número de tickets de entrada: "))
if n > 10:
    print("El número de tickets no debe exceder 10.")
else:
    for i in range(n):
        precio = float(input(f"Ingrese el precio del ticket {i+1}: "))
        total_recaudado += precio

    print("El total recaudado es:", total_recaudado)
