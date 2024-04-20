#Realizar un D.F. que permita ingresar los siguientes datos en una factura: Nombre y apellido de un cliente, fecha, cantidad, producto, precio. Luego visualizar en pantalla el neto, el iva y el total.

# Solicitar al usuario que ingrese los datos de la factura
nombre_cliente = input("Ingrese el nombre y el apellido del cliente: ")
fecha = input("Ingrese la fecha (DD/MM/AAAA): ")
cantidad = int(input("Ingrese la cantidad de productos: "))
producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))

# Calcular el neto, el IVA y el total de la factura
neto = cantidad * precio
iva = neto * 0.19
total = neto + iva

# Imprimir los detalles de la factura en pantalla
print("Nombre del cliente:", nombre_cliente)
print("Fecha:", fecha)
print("Cantidad:", cantidad)
print("Producto:", producto)
print("Precio unitario:", precio)
print("Neto:", neto)
print("IVA (19%):", iva)
print("Total:", total)