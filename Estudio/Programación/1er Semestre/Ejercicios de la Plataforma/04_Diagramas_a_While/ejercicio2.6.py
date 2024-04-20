# Crear un ALGORITMO que permita ingresar el PRECIO de 10 tickets de entrada
# para un evento.
# Finalmente mostrar el total recaudado
x = 1
totalPrecio = 0
while x <= 10:
    valor = int(input("Ingrese valor entrada: "))
    totalPrecio = totalPrecio + valor
    x = x + 1
print(totalPrecio)