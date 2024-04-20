lista = [
    [10, 2],
    [5, 3, 8],
    [7]
    ]

# print()
# print(lista[1][1])
# print()
# lista[1][1]=4
# print(lista[1][1])
# print()

# lista2 = [10, 20, 30, 40]
# lista2[1] = 80
# print(lista2[1])
# print()

for d1 in lista:
    txt = ""
    for d2 in d1:
        txt = txt + str(d2) + " "
    print(txt)

