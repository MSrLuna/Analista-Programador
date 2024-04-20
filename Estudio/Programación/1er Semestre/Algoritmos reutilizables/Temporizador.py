import time

def temporizador(segundos):
    while segundos > 0:
        time.sleep(1)
        segundos -= 1