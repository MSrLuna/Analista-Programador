i = 1
lista_o = "o"

while i <= 13:
    print(lista_o)
    if i < 7:
        lista_o = lista_o + "o"
    else:
        lista_o = lista_o[:-1]
    i = i + 1 