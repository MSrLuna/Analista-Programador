# Inicializar el total recaudado y el contador de entradas
total_recaudado = 0
contador_entradas = 0

# Mientras no se alcance el límite de 10 entradas, pedir el código y precio de la entrada
while contador_entradas < 10:
    codigo = input("Ingrese el código de la entrada: ")
    precio = float(input("Ingrese el precio de la entrada: "))
    
    # Validar que el precio sea mayor a cero
    if precio <= 0:
        print("El precio debe ser mayor a cero")
        continue
    
    # Sumar el precio de la entrada al total recaudado
    total_recaudado += precio
    
    # Incrementar el contador de entradas
    contador_entradas += 1

# Mostrar el total recaudado
print("El total recaudado es:", total_recaudado)