# Este programa calcula el descuento del 7,5% y el total final de una venta

# Se solicita al usuario que ingrese el monto de la venta y se convierte en un número entero
venta = int(input("Ingrese el monto de la venta: "))

# Se calcula el descuento del 7,5% aplicado a la venta
descuento = venta * 0.075

# Se calcula el total final de la venta con descuento
total_final = venta - descuento

# Se muestra el descuento aplicado en la pantalla utilizando la función "print()"
print("El descuento aplicado es de:", descuento)

# Se muestra el total final con descuento en la pantalla utilizando la función "print()"
print("El total final con descuento es de:", total_final)