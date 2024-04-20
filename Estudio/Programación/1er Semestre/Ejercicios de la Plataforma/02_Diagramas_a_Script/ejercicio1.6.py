#   Realizar un D.F. que permita ingresar los siguientes datos en una factura:
#   Nombre y apellido de un cliente, fecha, cantidad, producto, precio. Luego 
#   visualizar en pantalla el neto, el iva y el total.
nombre = input("Ingrese nombre: ")
apellido = input("Ingrese apellido: ")
fecha = input("Ingrese fecha: ")
precio = int(input("Cuál es el precio del producto? "))
cantidad = int(input("Cuál es la cantidad a comprar? "))

total = precio * cantidad
iva = total * 0.19
neto = total - iva
print("TOTAL COMPRA:", total)
print("IVA COMPRA:", iva)
print("NETO COMPRA:", neto)
