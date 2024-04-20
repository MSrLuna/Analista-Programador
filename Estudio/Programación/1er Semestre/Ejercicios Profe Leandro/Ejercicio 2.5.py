nombre = input("Ingrese el nombre del cliente: ")  # Pedimos el nombre del cliente
fono = input("Ingrese el fono del cliente: ")  # Pedimos el fono del cliente
estado_civil = input("Ingrese el estado civil del cliente: ")  # Pedimos el estado civil del cliente
if estado_civil == "soltero":  # Si el estado civil es soltero
    print("El cliente", nombre, "es soltero.")  # Mostramos un mensaje indicando que el cliente es soltero
elif estado_civil == "casado":  # Si el estado civil es casado
    print("El cliente", nombre, "está casado.")  # Mostramos un mensaje indicando que el cliente está casado
elif estado_civil == "viudo":  # Si el estado civil es viudo
    print("El cliente", nombre, "es viudo.")  # Mostramos un mensaje indicando que el cliente es viudo
elif estado_civil == "divorciado":  # Si el estado civil es divorciado
    print("El cliente", nombre, "está divorciado.")  # Mostramos un mensaje indicando que el cliente está divorciado
else:  # Si el estado civil no corresponde a ninguna de las opciones anteriores
    print("Estado civil inválido.")  # Mostramos un mensaje indicando que el estado civil es inválido