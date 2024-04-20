# Solicitar al usuario que ingrese las notas separadas por comas
notas_ingresadas = input("Ingrese las notas separadas por comas: ")

# Dividir las notas ingresadas en una lista utilizando la coma como separador
notas = notas_ingresadas.split(",")

# Convertir los elementos de la lista de notas a números enteros
notas = [int(nota) for nota in notas]

# Calcular la suma de las notas
suma = sum(notas)

# Obtener la cantidad de notas
cantidad = len(notas)

# Calcular el promedio
promedio = suma / cantidad

# Imprimir el resultado del promedio
print("El promedio de notas es:", promedio)