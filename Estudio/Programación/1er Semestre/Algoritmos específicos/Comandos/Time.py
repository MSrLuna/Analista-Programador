import time

# Devuelve el número de segundos transcurridos desde la época Unix hasta el momento actual
tiempo_actual = time.time()

# Hace que el programa se detenga durante la cantidad de segundos especificada
time.sleep(segundos)

# Devuelve el tiempo actual como una estructura de tiempo local
tiempo_local = time.localtime()

# Convierte un objeto de tiempo en una cadena de texto formateada
tiempo_formateado = time.strftime(formato, tiempo)

# Convierte un número de segundos desde la época Unix en una estructura de tiempo UTC
tiempo_utc = time.gmtime(segundos)

# Convierte una estructura de tiempo en el número de segundos desde la época Unix
segundos_desde_epoca = time.mktime(tiempo)