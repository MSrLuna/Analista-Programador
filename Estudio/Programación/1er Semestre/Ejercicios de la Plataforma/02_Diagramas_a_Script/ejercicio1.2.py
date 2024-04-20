#   Se requiere ingresar una venta por teclado, aplicar un 7,5% de descuento a 
#   esa venta, después mostrar en pantalla, el descuento y el total final.

# input imprime el texto que le demos, sin necesidad de usar print
# además, captura el valor que el usuario ingrese por teclado
valorVenta = int(input("Ingrese total de la venta "))
valorDescuento = valorVenta * 0.075
total = valorVenta - valorDescuento
print(total)