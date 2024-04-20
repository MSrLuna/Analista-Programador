opcion = 1
# mientras la opción sea 1 se repetirá el while
# tengo que hacer que la persona ingrese el valor a opcion al final del while
while opcion == 1:
    # creo las variables ANTES del try.. por si try detecta un error antes de la
    # modificación de las variables.. así ya las tengo previamente definidas
    suma = 0
    resta = 0
    multiplicacion = 0
    division = 0
    # el bloque TRY nos sirve para tener dentro un código que podría causar un error
    try:
        num1 = int(input("Ingrese número 1: "))
        num2 = int(input("Ingrese número 2: "))
    
        suma = num1 + num2
        resta = num1 - num2
        multiplicacion = num1 * num2
        # por ejemplo, una división por el número cero produce un error
        division = num1 / num2
    except ZeroDivisionError:
        # Podemos ser específicos al CAPTURAR un tipo de error determinado
        division = "No puede dividir por cero"
        print("ERROR al intentar dividir por cero")
    except ValueError:
        print("Se esperaba que ingresara un número, no un símbolo ni letra.")
    except:
        # Si se produce un error, entrarará en este bloque. Sino, no entrará.
        # except solo, captura todos los errores, pero no podremos identificar
        # cuál fue el error por el que cayó el código
        print("Otro tipo de error")

    # print("La suma es", suma)
    # Otra forma de mezclar texto con variables es usando f antes de las comillas
    # y poniendo estre llaves {} el nombre de la variable
    print(f"La suma es {suma}")
    print(f"La resta es {resta}")
    print(f"La multiplicación es {multiplicacion}")
    print(f"La división es {division}")

    # Aquí me aseguro de que la persona decida si el ciclo continuará o se detendrá
    opcion = int(input("Ingrese 1 si desea continuar... "))