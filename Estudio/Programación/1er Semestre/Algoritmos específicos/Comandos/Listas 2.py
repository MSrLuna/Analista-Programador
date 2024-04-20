# Ejercicio: Gestión de una lista de tareas

# Creamos una lista vacía para almacenar nuestras tareas
lista_tareas = []

# Agregamos algunas tareas iniciales a la lista
lista_tareas.append("Comprar víveres")
lista_tareas.append("Hacer ejercicio")
lista_tareas.append("Llamar al médico")

# Mostramos la lista de tareas actual
print("Lista de tareas:")
for tarea in lista_tareas:
    print("- " + tarea)

# Accedemos y modificamos una tarea existente
indice = 1
print("\nModificando tarea en el índice", indice)
tarea_modificada = "Hacer ejercicio en casa"
lista_tareas[indice] = tarea_modificada

# Mostramos la lista de tareas actualizada
print("\nLista de tareas actualizada:")
for tarea in lista_tareas:
    print("- " + tarea)

# Agregamos una nueva tarea al final de la lista
nueva_tarea = "Enviar correo electrónico"
lista_tareas.append(nueva_tarea)

# Mostramos la lista de tareas actualizada
print("\nLista de tareas actualizada:")
for tarea in lista_tareas:
    print("- " + tarea)

# Insertamos una tarea en una posición específica
nueva_tarea = "Llamar al banco"
indice = 2
print("\nInsertando tarea en el índice", indice)
lista_tareas.insert(indice, nueva_tarea)

# Mostramos la lista de tareas actualizada
print("\nLista de tareas actualizada:")
for tarea in lista_tareas:
    print("- " + tarea)

# Eliminamos una tarea por valor
tarea_eliminar = "Llamar al médico"
print("\nEliminando tarea:", tarea_eliminar)
lista_tareas.remove(tarea_eliminar)

# Mostramos la lista de tareas actualizada
print("\nLista de tareas actualizada:")
for tarea in lista_tareas:
    print("- " + tarea)

# Eliminamos una tarea por índice
indice_eliminar = 0
print("\nEliminando tarea en el índice", indice_eliminar)
del lista_tareas[indice_eliminar]

# Mostramos la lista de tareas actualizada
print("\nLista de tareas actualizada:")
for tarea in lista_tareas:
    print("- " + tarea)

# Obtenemos la longitud de la lista de tareas
longitud = len(lista_tareas)
print("\nLongitud de la lista de tareas:", longitud)

# Comprobamos si una tarea está en la lista
tarea_buscar = "Hacer ejercicio en casa"
if tarea_buscar in lista_tareas:
    print("\nLa tarea", tarea_buscar, "está en la lista.")
else:
    print("\nLa tarea", tarea_buscar, "no está en la lista.")

# Revertimos el orden de las tareas
lista_tareas.reverse()

# Mostramos la lista de tareas en orden invertido
print("\nLista de tareas en orden invertido:")
for tarea in lista_tareas:
    print("- " + tarea)

# Ordenamos las tareas alfabéticamente
lista_tareas.sort()

# Mostramos la lista de tareas ordenadas
print("\nLista de tareas ordenadas:")
for tarea in lista_tareas:
    print("- " + tarea)