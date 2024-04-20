#Paso 1: importar la librería para conectarnos con Oracle.
import cx_Oracle

#Paso 2: datos para conectarnos con la base de datos.
usuario = "INACAP"
contrasena = "inacap"
dsn = "localhost/xe"

#Paso 3: nos conectamos con la base de datos.
conexion = cx_Oracle.connect(user=usuario, password=contrasena, dsn=dsn)

#Paso 4: creamos una hoja donde podamos ejecutar consultas, usando cursor().
hoja = conexion.cursor()

#Paso 5: Ejecutamos una sentencia.
query = "SELECT * FROM jobs WHERE max_salary > 10000"
hoja.execute(query)

#Paso 6: Si lo que ejecutamos fue un SELECT, entonces tenermos que obtener sus resultados
#utilizando fetchall()
resultados = hoja.fetchall()

#Paso 7: Recorrer todos los resultados usando for.

cnt = 0
for fila in resultados:
    #Recordatorio: fila va a guardar la tupla de datos del recorrido actual,
    #por ejemplo, en el primer recorrido, fila guarda el valor de resultado[0],
    #en el segundo recorrido, fila guardará el valor de resultados[1] y así sucesivamente
    #print(fila)

    #Ejercicio: modificar este código para que muestre el nombre del JOB y el salario
    #máximo, donde el salario máximo sea superior a 10000.
    print(fila[1])