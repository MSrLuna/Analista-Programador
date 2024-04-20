# Definimos una función llamada calcular_promedio
def calcular_promedio(lista):
    # Verificamos si la lista está vacía
    if len(lista) == 0:
        # Si la lista está vacía, devolvemos 0
        return 0
    
    # Sumamos todos los elementos de la lista
    suma = 0
    for numero in lista:
        suma += numero
    
    # Calculamos el promedio dividiendo la suma entre la cantidad de elementos
    promedio = suma / len(lista)
    
    # Devolvemos el promedio como resultado de la función
    return promedio

# Creamos una lista de ejemplo
numeros = [5, 10, 15, 20, 25]

# Llamamos a la función calcular_promedio y guardamos el resultado en una variable
resultado = calcular_promedio(numeros)

# Imprimimos el resultado
print("El promedio de la lista es:", resultado)