import cx_Oracle

usuario = "INACAP"
contrasena = "inacap"
dsn = "192.168.56.1"

conexion = cx_Oracle.connect(user=usuario, password=contrasena, dsn=dsn)

hoja = conexion.cursor()