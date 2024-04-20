# Realice el mismo ALGORITMO anterior que permita el Ingreso de 3 notas académicas (con uso de ciclo mientras).
# Validar notas entre 1,0 y 7,0, en caso contrario emitir mensaje de error “Fuera de rango permitido” y terminar.
# si las notas están dentro del rango, mostrar promedio final de notas.

notas = []  # Se inicializa una lista vacía llamada "notas".
i = 0  # Se inicializa una variable "i" con valor 0 para llevar el conteo de las notas ingresadas.
while i < 3:  # Se utiliza un ciclo while que se repetirá hasta que se ingresen las 3 notas requeridas.
    nota = float(input("Ingrese una nota académica: "))  # Se utiliza la función "input()" para pedirle al usuario que ingrese una nota académica como un número decimal y se convierte a un tipo de dato float para poder ser utilizado en comparaciones. La nota se almacena en la variable "nota".
    if nota < 1.0 or nota > 7.0:  # Se verifica si la nota está dentro del rango permitido, que es entre 1.0 y 7.0. 
        print("Error fuera de rango")  # Si la nota está fuera de este rango, se muestra un mensaje de "Error fuera de rango".
        break  # Se utiliza la instrucción "break" para salir del ciclo while si alguna nota está fuera del rango permitido.
    notas.append(nota)  # Si la nota está dentro del rango permitido, se agrega a la lista "notas".
    i += 1  # Se aumenta el valor de "i" en 1 para llevar el conteo de las notas ingresadas.

if len(notas) == 3:  # Si se ingresaron las 3 notas requeridas y todas están dentro del rango permitido, se procede a calcular el promedio.
    promedio = sum(notas) / len(notas)  # Se calcula el promedio de las tres notas sumándolas y dividiendo por 3, y se almacena en la variable "promedio".
    print("El promedio de las notas es:", promedio)  # Finalmente, se muestra el promedio de las notas utilizando la función "print()".