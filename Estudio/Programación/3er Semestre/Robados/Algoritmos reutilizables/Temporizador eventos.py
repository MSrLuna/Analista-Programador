import time

def evento():
    print("¡Evento ejecutado!")

tiempo_espera = 1  # Tiempo en segundos antes de ejecutar el evento
time.sleep(tiempo_espera)
evento()
