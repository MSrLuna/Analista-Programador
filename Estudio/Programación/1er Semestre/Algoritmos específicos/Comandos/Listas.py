#Crear una lista vacía:
lista = []

#Crear una lista con elementos:
lista = [1, 2, 3, 4, 5]

#Acceder a un elemento de la lista por índice:
elemento = lista[2]

#Modificar un elemento de la lista por índice:
lista[1] = 10

#Agregar un elemento al final de la lista:
lista.append(6)

#Insertar un elemento en una posición específica:
lista.insert(2, 7)

#Eliminar un elemento de la lista por valor:
lista.remove(3)

#Eliminar un elemento de la lista por índice:
del lista[4]
lista.pop(4)

#Obtener la longitud de la lista (número de elementos):
longitud = len(lista)

#Comprobar si un elemento está en la lista:
if 5 in lista:
    print("El elemento 5 está en la lista.")

#Revertir el orden de los elementos en la lista:
lista.reverse()

#Ordenar los elementos de la lista en orden ascendente:
lista.sort()

#Obtener el índice de la primera aparición de un elemento:
indice = lista.index(4)

#Contar el número de veces que un elemento aparece en la lista:
contador = lista.count(2)

