# Inicializamos la variable suma con 0
suma = 0

# Utilizamos un ciclo for para iterar 5 veces
for i in range(5):
    
    # Pedimos al usuario que ingrese un número y lo convertimos a float
    numero = float(input("Ingrese un número: "))
    
    # Sumamos el número ingresado a la variable suma
    suma += numero
    
    # Mostramos en pantalla la sumatoria acumulada hasta el momento
    print("La sumatoria acumulada es:", suma)