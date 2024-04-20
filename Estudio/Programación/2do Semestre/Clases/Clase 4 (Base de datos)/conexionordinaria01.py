import cx_Oracle

#usuario que se le dio cuando creamos.
usuario = "INACAP"

#contraseña que se le dio a este usuario cuando lo creamos.
contrasena = "inacap"

#dsn, corresponde a la combinación de 2 valores:
#1. La ip donde está escuchando el servicio de Oracle, en el caso de localhost.
#2. Después de un slash, pondremos el SID (ir a mirar a SQLdeveloper).
direccion = "localhost/xe"

conexion = cx_Oracle.connect(user=usuario, password=contrasena, dsn=direccion)

#Hasta este punto, tenemos la conexión establecida, pero por decirlo de alguna manera
#nos falta tener una hoja de trabajo, sobre lo que escribiremos las consultas y las demás.
#Más tecnicamente hablando, cursor() te permitirá ejecutar comandos SQL.
HojaDeTrabajo = conexion.cursor()

#A través del objeto que retornó cursor() podremos llamar a los métodos que ejecutamos.
HojaDeTrabajo.execute("SELECT * FROM departments")

#Los datos quedarán guardados temporalmente en la variable del cursor, en este caso hoja de trabajo.
#Si queremos obtenerlos, necesitamos ejecutar un método extra, que dependerá de cuantos datos
#podamos recibir:
#1. Si esperamos recibir muchos datos, usamos fetchall().
#2. Si queremos recibir UN dato, usamos fetchone().
filas = HojaDeTrabajo.fetchall()

for fila in filas:
    print(fila[1])

for fila in filas:
    idDepto = fila[0]
    nombreDepto = fila[1]
    idManager = fila[2]
    idLocation = fila[3]
    print(f"ID: {idDepto}, Departamento: {nombreDepto}.")