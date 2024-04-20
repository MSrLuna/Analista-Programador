#Crear un D.F que permita visualizar los primeros 15 múltiplos de 8, ordenados ascendentemente. (Estructura de control: Mientras)

i = 1
contador = 0

while contador < 15:
    if i % 8 == 0:
        print(i)
        contador += 1
    i += 1