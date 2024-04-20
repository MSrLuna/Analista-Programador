# El ciclo WHILE es el Mientras de PseInt
# Repite todo el código que tiene dentro, MIENTRAS la condición que le hayamos
# entregado sea True.. es una condición como las que ponemos en los IF
# Típicamente le pondremos un contador que se vaya sumando dentro del While para que tenga fin
contador = 5
# mientras la variable contador sea menor a 10 se repetirá el ciclo
while contador < 10:
    # imprimo el valor en pantalla
    print(contador)
    # hago que contador vaya aumentando su valor, para que la condición del while
    # en algún momento de falso y así se rompa el ciclo
    contador = contador + 2