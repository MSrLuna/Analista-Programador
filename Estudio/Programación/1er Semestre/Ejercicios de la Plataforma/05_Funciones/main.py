# Aprendiendo a usar funciones en Python
# Una función es una porción de código guardada bajo un nombre específico
# Cada vez que llamamos a ese nombre, estaremos ejecutando todo ese código

# Por ejemplo, podríamos crear una función para saludar

# Comenzamos con la palabra def y luego asignamos el nombre de la función
# Ponemos paréntesis y el símbolo dos puntos, para indicar que comenzamos la función
def saludar():
    print("HOLA!!")

# Si ahora (afuera de la función) llamamos a saludar() se ejecutará la línea 10
saludar()

# Como pueden ver, si ejecutan el código hasta este punto, ejecutará el print de la línea 10
# Las funciones también pueden recibir parámetros, o sea, variables que vienen
# desde fuera de la función, que no existen dentro de ella..

# Esta función está esperando que, cuando la llames, le pases una variable
def saludarPersona(nombre):
    # aquí dentro va a usar la variable nombre para concatenarla en el print
    # nombre puede tener cualquier valor.. ese valor se define cuando llamas a la función
    print("Hola", nombre)

# Llamemos a la función saludarPersona y entreguémosle un valor por paréntesis
saludarPersona("Gabriel")

# Si ejecutaste el código en este punto, verás que ahora el resultado es "Hola Gabriel"
# En otras palabras está ejecutando la línea 23 y en nombre está poniendo el valor
# que pusimos en la línea 26 entre paréntesis.. nombre absorbe lo que pongamos en
# los paréntesis cuando llamamos a la función

# Que tal si ahora lo hacemos de acuerdo a lo que el cliente ingrese por teclado?
nom = input("Ingrese nombre para ser saludado... ")
saludarPersona(nom)

# Ves que ahora está saludando a lo que hayas puesto al ingresar algo por teclado?

# Ahora, intenta hacer una función que espere recibir un número
# Dentro de la función tienes que averiguar si ese número que se recibió es
# positivo o negativo. De acuerdo a eso, imprimir en pantalla positivo o negativo.