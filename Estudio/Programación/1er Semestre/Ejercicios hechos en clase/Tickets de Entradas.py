# Inicializar el total recaudado y el contador de entradas
total_recaudado = 0
contador_entradas = 0

# Mientras no se alcance el límite de 10 entradas, pedir el código y precio de la entrada
while contador_entradas < 10:
	codigo = input("Ingrese el código de la entrada: ")
	precio = float(input("Ingrese el precio de la entrada: "))
	
	# Validar que el precio sea mayor a cero
	if precio > 0:
		total_recaudado += precio
		contador_entradas += 1
	else:
		print("El precio debe ser mayor a cero")

# Mostrar el total recaudado
print("El total recaudado es:", total_recaudado)