# Este programa permite al usuario ingresar las ventas anuales de un negocio (1 por mes) y muestra el promedio anual

# Se inicializa una variable "suma_ventas" con un valor de 0
suma_ventas = 0

# Se utiliza un ciclo "for" para solicitar al usuario las ventas de cada mes (12 meses en total)
for mes in range(1, 13):
    venta = float(input("Ingrese la venta del mes {}: ".format(mes)))  # Se solicita la venta del mes actual
    suma_ventas += venta  # Se agrega la venta actual a la suma total de ventas

# Se calcula el promedio anual dividiendo la suma total de ventas entre 12
promedio_anual = suma_ventas / 12

# Se muestra el promedio anual en la pantalla utilizando la función "print()"
print("El promedio anual de ventas es:", promedio_anual)