# Una función básica no te retorna nada, solo ejecuta líneas de código
def saludar():
    print("Hola sin retorno")

# Una función también puede RETORNAR un valor.. eso se puede guardar en una variable
# que llame a la función
def saludarConRetorno():
    x = 10
    y = 5
    total = 10 * 20 / x
    # La clave está en usar la palabra return
    return total

# saludar()
# resultado = saludarConRetorno()

def sumar(num1, num2):
    resultado = num1 + num2
    return resultado

n1 = int(input("Ingrese número 1: "))
n2 = int(input("Ingrese número 2: "))
valorRetornado = sumar(n1, n2)
print(valorRetornado)