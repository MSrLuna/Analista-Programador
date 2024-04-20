# Este programa comprueba si un número ingresado por el usuario está dentro del rango de 5 a 10

# Se solicita al usuario que ingrese un número y se convierte en un número decimal utilizando la función "float()"
numero = float(input("Ingrese un número: "))

# Se utiliza una estructura "if-else" para comprobar si el número ingresado está dentro del rango de 5 a 10
if numero > 5 and numero <= 10:
    print("Correcto")  # Si el número está dentro del rango, se muestra el mensaje "Correcto" en la pantalla
else:
    print("Fuera de rango")  # Si el número está fuera del rango, se muestra el mensaje "Fuera de rango" en la pantalla