# Almacenamiento de datos en memoria ingresados por teclado
arreglo = []
tupla = ()
diccionario = {}
anidado = {}

# Ingreso de datos por teclado
num_elementos = int(input("Ingrese el número de elementos para el arreglo: "))
for i in range(num_elementos):
    elemento = int(input(f"Ingrese el elemento {i+1}: "))
    arreglo.append(elemento)

num_elementos = int(input("Ingrese el número de elementos para la tupla: "))
for i in range(num_elementos):
    elemento = input(f"Ingrese el elemento {i+1}: ")
    tupla += (elemento,)

num_elementos = int(input("Ingrese el número de pares clave-valor para el diccionario: "))
for i in range(num_elementos):
    clave = input(f"Ingrese la clave {i+1}: ")
    valor = input(f"Ingrese el valor para la clave '{clave}': ")
    diccionario[clave] = valor

# Construcción del diccionario anidado
anidado['arreglo'] = arreglo
anidado['tupla'] = tupla
anidado['diccionario'] = diccionario

# Recorrido y visualización de los datos ingresados
print("Elementos del arreglo:")
for elemento in arreglo:
    print(elemento)

print("\nElementos de la tupla:")
for elemento in tupla:
    print(elemento)

print("\nElementos del diccionario:")
for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")

print("\nElementos del diccionario anidado:")
for clave, valor in anidado.items():
    print(f"{clave}:")
    if isinstance(valor, list) or isinstance(valor, tuple):
        for elemento in valor:
            print(f"\t{elemento}")
    elif isinstance(valor, dict):
        for k, v in valor.items():
            print(f"\t{k}: {v}")
    else:
        print(f"\t{valor}")
