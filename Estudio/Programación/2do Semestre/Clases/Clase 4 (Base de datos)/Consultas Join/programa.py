from conexion import hoja

#En caso de querer mostrar más de una columna hay que hacer join ya que esto producirá que vengan
#más columnas de datos, así que por regla general si usamos JOIN no usaremos SELECT *, porque vendrán 
#demasiadas columnas de datos.
sql = f'''
        SELECT first_name, last_name, department_name FROM employees
        INNER JOIN departments on departments.department_id = employees.department_id
        '''
hoja.execute(sql)
resultados = hoja.fetchall()

for fila in resultados:
    print(fila)