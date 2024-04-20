import cx_Oracle

USER = "INACAP"
PASSWORD = "inacap"
DSN = "192.168.56.1"

conexion = cx_Oracle.connect(user=USER,password=PASSWORD,dsn=DSN)
hoja = conexion.cursor()