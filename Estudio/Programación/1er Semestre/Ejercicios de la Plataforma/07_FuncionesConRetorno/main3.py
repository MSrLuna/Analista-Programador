def obtenerPromedio(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio

# HACER el mismo ejercicio, pero ahora debe validar que los valores ingresados
# no son vacíos. Solicitar el número hasta que ingrese algo correctamente.

interruptor = True
while interruptor:
    try:
        n1 = int(input("Ingrese nota 1: "))
        n2 = int(input("Ingrese nota 2: "))
        n3 = int(input("Ingrese nota 3: "))

        interruptor = False
    except:
        print("No puede ingresar algo que no sea un número...")
        print("Vuelva a intentar")


# Tampoco debe permitir letras