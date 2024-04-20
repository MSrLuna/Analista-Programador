from datetime import datetime, timedelta

# Devuelve un objeto `datetime` que representa la fecha y hora actuales
fecha_actual = datetime.now()

# Crea un objeto `datetime` con los valores especificados
fecha_personalizada = datetime(year, month, day, hour, minute, second)

# Representa una duración o diferencia entre dos puntos en el tiempo
duracion_tiempo = timedelta(days, hours, minutes, seconds)

# Devuelve una cadena de texto formateada de acuerdo con el formato especificado, a partir de un objeto `datetime`
cadena_formateada = datetime.strftime(formato)

# Convierte una cadena de texto en un objeto `datetime`, según el formato especificado
fecha_desde_cadena = datetime.strptime(cadena, formato)