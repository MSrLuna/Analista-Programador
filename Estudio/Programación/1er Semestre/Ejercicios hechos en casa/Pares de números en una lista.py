#Encontrar todos los pares de números en una lista cuya suma sea igual a un valor objetivo dado:
def encontrar_pares(lista, objetivo):
    pares = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == objetivo:
                pares.append((lista[i], lista[j]))
    return pares
