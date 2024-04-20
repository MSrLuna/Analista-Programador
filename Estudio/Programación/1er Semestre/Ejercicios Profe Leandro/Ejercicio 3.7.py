#Crear un D.F. que permita ingresar 10 ticket de entradas (código, precio), para un evento. Al finalizar los ingresos visualizar la suma total de precios de la venta. Si la venta total asciende los $20.000 aplicar un descuento de 8,5% mostrar el resultado de la venta final con descuento aplicado. (Debe controlar la cantidad de ingresos mediante una estructura de control.)

total_venta = 0
for i in range(10):
    codigo = input("Ingrese el código del ticket: ")
    precio = float(input("Ingrese el precio del ticket: "))
    total_venta += precio

if total_venta > 20000:
    descuento = total_venta * 0.085
    total_venta -= descuento

print("El total de la venta es:", total_venta)