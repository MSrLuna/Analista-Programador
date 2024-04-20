import cx_Oracle

USUARIO = "INACAP"
PASSWORD = "inacap"
DSN = "localhost/xe"

conexion = cx_Oracle.connect(user=USUARIO, password=PASSWORD, dsn=DSN)
hoja = conexion.cursor()