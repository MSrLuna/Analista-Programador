# BLOQUES CONDICIONALES IF - ELSE
# Después de usar la palabra reservada if, escribimos una expresión booleana
# Esto quiere decir, que la expresión debe devolver un valor True o False
# Finalmente ponemos el símbolo "2 puntos" y creamos una nueva línea
if 10 > 5:
    # IMPORTANTÍSIMO!!!!!!!!
    # Cuando creamos un nuevo bloque (if, for, while), debemos respetar el espacio al inicio
    # Un if DEBE TENER al menos una línea de código
    print("Entro en la parte TRUE del IF")
else:
    # Cuando la expresión booleana devuelva False, entraremos en el bloque else
    print("Entro a la parte FALSE del IF")

# Si me quiero salir del bloque IF o del ELSE, borro la sangría..

# Validemos que el número 1 sea mayor al número 2
num1 = input("Ingrese número 1: ")
num2 = input("Ingrese número 2: ")
# Para comparar si 2 valores son IGUALES, ponemos 2 veces signo igual
if num1 == num2:
    print("Son iguales")
else:
    # Si no son igual, empiezo a preguntar si uno 
    if num1 > num2:
        print("num1 es mayor a num2")
    else:
        print("num2 es menor a num1")