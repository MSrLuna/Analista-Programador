# Realice un ALGORITMO que permita el Ingreso de 3 notas académicas (sin ciclo).
# Usando 3 variables para cada número. - Validar notas entre 1,0 y 7,0, en caso contrario emitir mensaje de error “Fuera de rango permitido” y terminar.
# si las notas están dentro del rango, mostrar promedio final de notas.

nota1 = float(input("Ingrese la primera nota: "))  # Se utiliza la función "input()" para pedirle al usuario que ingrese la primera nota académica como un número decimal y se convierte a un tipo de dato float para poder ser utilizado en comparaciones. La nota se almacena en la variable "nota1".
nota2 = float(input("Ingrese la segunda nota: "))  # Se utiliza la función "input()" para pedirle al usuario que ingrese la segunda nota académica como un número decimal y se convierte a un tipo de dato float para poder ser utilizado en comparaciones. La nota se almacena en la variable "nota2".
nota3 = float(input("Ingrese la tercera nota: "))  # Se utiliza la función "input()" para pedirle al usuario que ingrese la tercera nota académica como un número decimal y se convierte a un tipo de dato float para poder ser utilizado en comparaciones. La nota se almacena en la variable "nota3".

if nota1 < 1.0 or nota1 > 7.0 or nota2 < 1.0 or nota2 > 7.0 or nota3 < 1.0 or nota3 > 7.0:  # Se verifica si las notas están dentro del rango permitido, que es entre 1.0 y 7.0. 
    print("Fuera de rango permitido")  # Si alguna nota está fuera de este rango, se muestra un mensaje de "Fuera de rango permitido".
else:
    promedio = (nota1 + nota2 + nota3) / 3  # Si todas las notas están dentro del rango permitido, se calcula el promedio de las tres notas sumándolas y dividiendo por 3, y se almacena en la variable "promedio".
    print("El promedio de las notas es:", promedio)  # Finalmente, se muestra el promedio de las notas utilizando la función "print()".