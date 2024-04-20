import time

def temporizador(segundos):
    while segundos > 0:
        print(segundos)
        time.sleep(1)
        segundos -= 1
    print("¡Tiempo finalizado!")

segundos_ingresados = int(input("Ingrese el número de segundos para el temporizador: "))
temporizador(segundos_ingresados)