matrizA = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrizB = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

resultado = []

for i in range(len(matrizA)):
    fila_resultado = []
    for j in range(len(matrizA[i])):
        suma = matrizA[i][j] + matrizB[i][j]
        fila_resultado.append(suma)
    resultado.append(fila_resultado)

print()

# Imprimir los resultados en filas de 3x3
for i in range(len(resultado)):
    for j in range(len(resultado[i])):
        print(resultado[i][j], end=' ')
        if (j+1) % 3 == 0:
            print()
    print()