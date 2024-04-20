#Ingresar los datos nombres, apellido de un curso de 25. Luego visualizar la cantidad de nombres “maría” y “Jose” existentes en el curso.

curso = [] # Creamos una lista vacía para almacenar los datos de los estudiantes
contador_maria = 0 # Inicializamos el contador de nombres "María" en cero
contador_jose = 0 # Inicializamos el contador de nombres "José" en cero

# Usamos un bucle for para pedir los datos de cada estudiante y agregarlos a la lista curso
for i in range(25):
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    curso.append([nombre, apellido])
    
# Usamos otro bucle for para recorrer la lista curso y contar la cantidad de nombres "María" y "José"
for estudiante in curso:
    if estudiante[0].lower() == "maría": # Convertimos el nombre a minúsculas para compararlo sin importar las mayúsculas
        contador_maria += 1
    elif estudiante[0].lower() == "josé": # Convertimos el nombre a minúsculas para compararlo sin importar las mayúsculas
        contador_jose += 1

# Mostramos en pantalla la cantidad de nombres "María" y "José" encontrados en la lista curso
print("Cantidad de nombres María:", contador_maria)
print("Cantidad de nombres José:", contador_jose)