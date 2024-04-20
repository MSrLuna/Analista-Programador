import time

inicio = time.time()

# Código cuya ejecución se va a medir
for i in range(300000000):
    pass

fin = time.time()
duracion = fin - inicio
print("La duración de ejecución fue de:", duracion, "segundos")