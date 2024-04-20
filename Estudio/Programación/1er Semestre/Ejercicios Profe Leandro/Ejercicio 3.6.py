#Realice un D.F, que permita ingresar 10 números-(Uso Estructura de control: Mientras) - Cada vez que se ingrese un número mostrarlo en pantalla. - Una vez ingresados los 10 números emitir un mensaje “Los 10 números ya se han ingresado satisfactoriamente”

contador = 1
while contador <= 10:
    numero = int(input("Ingrese un número: "))
    print(numero)
    contador += 1

print("Los 10 números ya se han ingresado satisfactoriamente")