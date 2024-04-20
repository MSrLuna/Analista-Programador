# Hacer el ejercicio de cálculo de promedio, pero esta vez sin funciones
# Calcular N cantidad de notas a promediar, donde N será ingresado por teclado
cantidadNotas = int(input("Cuántas notas se ingresarán?"))
totalNotas = 0
contador = 0
while contador < cantidadNotas:
    notaIngresada = float(input("Ingrese nota: "))
    totalNotas = totalNotas + notaIngresada
    contador = contador + 1

promedio = totalNotas / cantidadNotas
print(promedio)