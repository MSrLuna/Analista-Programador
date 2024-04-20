try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No puedes dividir entre cero.")

#Los bloques try y except se utilizan para manejar errores en tiempo de ejecución.
#Si ocurre un error en el bloque try, el control se traslada al bloque except correspondiente.