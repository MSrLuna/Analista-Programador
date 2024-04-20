#Crear un D.F que permita visualizar los primeros 10 números pares, ordenados ascendentemente. (Estructura de control: repetir-hasta)

n = 1
cont = 0

while cont < 10:
    if n % 2 == 0:
        print(n)
        cont += 1
    n += 1