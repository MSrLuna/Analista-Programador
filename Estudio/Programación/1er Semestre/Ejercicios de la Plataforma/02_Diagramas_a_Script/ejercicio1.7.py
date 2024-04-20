#   Crear un DF que permita ingresar 3 notas académicas. En caso de que 
#   alguna nota no corresponda al rango correcto, mostrar un mensaje “Error fuera 
#   de rango” y finalizar.

# CÓMO HACERLO
#Pedir primero que se ingresen las notas y guardarlas en variables
nota1 = float(input("Ingrese nota 1: "))
nota2 = float(input("Ingrese nota 2: "))
nota3 = float(input("Ingrese nota 3: "))

# Preguntar a cada una de esas notas si son mayor o igual a 1 y menor o igual a 7
#if nota1 >= 1 and nota1 <= 7 and nota2 >= 1 and nota2 <= 7 and nota3 >= 1 and nota3 <= 7:
    # Si nunca cae en false, hacer el cálculo del promedio y guardarlo en una variable
#    promedio = (nota1 + nota2 + nota3) / 3
    # Mostrar con print el promedio guardado en una variable
#    print(promedio)
#else:
#    print("ERROR")

if nota1 >= 1 and nota1 <= 7:
    if nota2 >= 1 and nota2 <= 7:
        if nota3 >= 1 and nota3 <= 7:
            promedio = (nota1 + nota2 + nota3) / 3
            print("Promedio: ", promedio)
        else:
            print("Error en nota3")
    else:
        print("Error en nota2")
else:
    print("Error en nota1")