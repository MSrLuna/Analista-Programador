def sumar(n1, n2):
    resultado = n1 + n2
    print("Resultado: ", resultado)

def restar(n1, n2):
    resultado = n1 - n2
    print("Resultado: ", resultado)

# HACER UNA FUNCIÓN QUE, RECIBIENDO 2 NÚMEROS, CALCULE LA POTENCIA
# DE ESE NÚMERO CON UN CICLO WHILE
def potencia(base, exponente):
    resultado = base
    x = 1
    while x < exponente:
        resultado = (base * resultado)
        x = x+1
    
    print("Resultado:", resultado)