notas = []  # se crea una lista vacía para almacenar las notas ingresadas

# se utiliza un ciclo for para iterar 3 veces (por las 3 notas a ingresar)
for i in range(3):
    
    # se utiliza un ciclo while para validar cada nota ingresada
    while True:
        nota = float(input("Ingrese una nota académica: "))  # se solicita al usuario ingresar una nota y se convierte a float
        
        if nota < 1.0 or nota > 7.0:  # se verifica si la nota ingresada está dentro del rango permitido
            print("Error fuera de rango permitido")  # si la nota está fuera del rango permitido se emite un mensaje de error
        else:
            notas.append(nota)  # si la nota es válida, se agrega a la lista "notas"
            break  # se rompe el ciclo while
    
# se calcula el promedio utilizando la función sum() para sumar las notas y len() para obtener la longitud de la lista "notas"
promedio = sum(notas) / len(notas)

# se imprime en pantalla el promedio final de notas utilizando la función print()
print("El promedio de las notas es:", promedio)