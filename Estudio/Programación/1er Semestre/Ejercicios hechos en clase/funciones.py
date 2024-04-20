def suma2n(num1, num2):
    Resultado = num1 + num2
    print("Resultado:", Resultado)

def elevación(elevado):
    contador = 1
    numerito = 1
    while contador <= 2:
        numerito = elevado * numerito
        contador = contador + 1
    print("Resultado: {}".format(numerito))