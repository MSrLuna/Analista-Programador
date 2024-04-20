import time

duracion = 1  # Duración en segundos del bucle
tiempo_inicio = time.time()

while time.time() - tiempo_inicio < duracion:
    # Código del bucle
    print("Ejecutando bucle...")

print("Bucle finalizado")