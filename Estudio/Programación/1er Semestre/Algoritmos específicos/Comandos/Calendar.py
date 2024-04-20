import calendar

# Devuelve una representación del mes especificado como una cadena multilinea
mes_formateado = calendar.month(year, month)

# Lista de nombres de los meses
nombres_meses = calendar.month_name

# Lista de nombres de los días de la semana
nombres_dias_semana = calendar.day_name

# Verifica si un año es bisiesto
es_bisiesto = calendar.isleap(year)

# Devuelve el día de la semana (0 a 6, donde 0 es lunes) para una fecha dada
dia_semana = calendar.weekday(year, month, day)
