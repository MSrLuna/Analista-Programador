lista = [ 
    10, 20, 40, 5, 8,
    {"nombre": "pedro", "apellido": "redlick"},
    ("durazno", "melón", "pera", "manzana")
]

print(lista)
print()

print(lista[3])

#----------

diccionario = lista[5]
print(diccionario["nombre"])

print(lista[5]["nombre"])

#----------

tupla = lista[6]
print(tupla[0])

print(lista[6][0])

print()

datos = [ 
    ["durazno", "manzana", "pera"],
    ["espinacas", "lechuga"],
    ["papas", "jenjíbre", "zanahoria"]
]
print(datos)
print()

print(datos[0][0])

#----------

print(datos[1][0])

#----------

print(datos[2][0])

print()

x = [[5, 2, 3,], 
     [1, 8, 6], 
     [4, 9, 7]
     ]
print(x)
print()
r = x[0][2] + x[1][1] + x[2][0]
print(r)
print()