# Imprimir en pantalla "Pasó de Curso" si es que el promedio de notas
# es superior o igual a 4

# Usar esta función para obtener el promedio
def obtenerPromedio(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio

# TERMINAR EJERCICIO
n1 = float(input("Ingresa nota 1: "))
n2 = float(input("Ingresa nota 2: "))
n3 = float(input("Ingresa nota 3: "))

prom = obtenerPromedio(n1, n2, n3)
if prom >= 4:
    print("Pasa de curso")
else:
    print("Te lo echaste po!")