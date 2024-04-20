#   Crear un D.F. permita ingresar la venta anual de un negocio (1 por cada 
#   mes), estos deben ser ingresados por teclado. Después imprimir por el 
#   promedio anual.

# Pido al usuario, con input, que se ingrese el total de ventas de Enero
# Encierro todo el input en los paréntesis de int, para transformar inmediatamente
# a número lo que ingresará el usuario..
ventasEnero = int(input("Ingresar total ventas Enero "))
ventasFebrero = int(input("Ingresar total ventas Febrero "))
ventasMarzo = int(input("Ingresar total ventas Marzo "))
ventasAbril = int(input("Ingresar total ventas Arbil "))
ventasMayo = int(input("Ingresar total ventas Mayo "))

# Ahora que tengo los valores ingresados dentro de las variables, las calculo
promedioAnual = (ventasEnero + ventasFebrero + ventasMarzo + ventasAbril + ventasMayo) / 5
# promedioAnual ahora tiene el promedio de ventas de los meses
# uso PRINT para imprimir en la consola el mensaje concatenado con la variable promedioAnual

# CUIDADO! si concatenas (usas el signo +) no podrás mezclar textos con números
# en un print.. para que funcione debes separar con coma, o bien, usar signo + y
# transformar promedioAnual en un tipo texto usando la función str()

# Opción con concatenación
print("Promedio de ventas de Enero a Mayo es de " + str(promedioAnual))
# Opción usando comas para juntar valores texto y número
print("Promedio de ventas de Enero a Mayo es de", promedioAnual)