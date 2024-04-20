import cx_Oracle

usuario = "INACAP"
contrasena = "inacap"
dsn = "localhost/xe"

conexion = cx_Oracle.connect(user=usuario, password=contrasena, dsn=dsn)

hoja = conexion.cursor()