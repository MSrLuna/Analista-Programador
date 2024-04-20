# Crear un DF que permita ingresar 3 notas académicas. 
# En caso de que alguna nota no corresponda al rango correcto, mostrar un mensaje “Error fuera de rango” y finalizar.

notas = []  # Se define una lista vacía llamada "notas" que se usará para almacenar las notas ingresadas por el usuario.

for i in range(3):  # Se utiliza un bucle "for" para pedir al usuario que ingrese una nota académica tres veces.
    nota = float(input("Ingrese una nota académica: "))  # Se utiliza la función "input()" para pedirle al usuario que ingrese una nota académica como un número decimal y se convierte a un tipo de dato float para poder ser utilizado en comparaciones.
    
    if nota < 1.0 or nota > 7.0:  # Se verifica si la nota está dentro del rango permitido, que es entre 1.0 y 7.0. 
        print("Error fuera de rango")  # Si la nota está fuera de este rango, se muestra un mensaje de "Error fuera de rango".
        break  # El programa termina utilizando el comando "break".
    
    notas.append(nota)  # Si la nota está dentro del rango permitido, se agrega a la lista "notas".
    
if len(notas) == 3:  # Después de que el bucle se completa, el código verifica si hay exactamente tres notas en la lista "notas".
    promedio = sum(notas) / len(notas)  # Se calcula el promedio de las tres notas utilizando la función "sum()" y se divide el resultado por la longitud de la lista "notas" utilizando el operador "/" y se almacena en la variable "promedio".
    print("El promedio de las notas es:", promedio)  # Finalmente, se muestra el promedio de las notas utilizando la función "print()".