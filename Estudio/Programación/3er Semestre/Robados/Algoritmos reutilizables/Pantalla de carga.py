import time
import sys

def pantalla_de_carga():
    duracion = 10  # Duración de la carga en segundos
    barra_ancho = 40  # Ancho de la barra de carga

    for i in range(barra_ancho + 1):
        progreso = i / barra_ancho
        barra = "█" * int(barra_ancho * progreso)
        espacios = " " * (barra_ancho - len(barra))
        tiempo_restante = int(duracion * (1 - progreso))

        sys.stdout.write(f"\r[{barra}{espacios}] {int(progreso * 100)}% ({tiempo_restante} segundos restantes)")
        sys.stdout.flush()
        time.sleep(duracion / barra_ancho)

    sys.stdout.write("\nCarga completa!\n")

if __name__ == "__main__":
    pantalla_de_carga()