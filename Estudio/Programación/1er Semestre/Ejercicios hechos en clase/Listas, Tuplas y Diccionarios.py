# Listas:

# notas = [1, 2, 3, 4, 5, 6, 7]
# suma = 0
# elementos = 0
# for X in notas:
#     suma = suma + X
#     elementos = elementos + 1
# prom = suma / elementos
# print(prom)

# notas = [1, 2, 3, 4, 5, 6, 7]
# prom = sum(notas) / len(notas)
# print(prom)

# Tuplas:

# tupla = (5, 2, 8, 7, 20)
# print(tupla[0])
# tupla = True
# print(tupla)

# a = 1
# b = 2
# c = 3
# d = 4
# e = 5

# tupla = (a, b, c, d, e)

# print(tupla)

# a = 5
# b = 4
# c = 3
# d = 2
# e = 1

# print(tupla)

# Diccionarios:
print()
abc = {"Nombre": "Franco", "Apellido": "Luna", "Alias": "Luna", "Edad": 18}
print(abc)
print(abc["Alias"])

abc["Alias"] = "Fala"
print()

print(abc)
print(abc["Alias"])
print()

abc["Ciudad"] = "Osorno"

print(abc)
print(abc["Ciudad"])
print()

edad = abc["Edad"] + 2
print(edad)
print()

abc["Edad"] = abc["Edad"] + 2
print(abc["Edad"])