from conexion import conexion, hojaSQL
class Usuario:

    def __init__(self):
        self.id = None
        self.nombre = None
        self.username = None
        self.email = None
    
    def insertar(self):
        sql = "INSERT INTO usuario (nombre, username, email) VALUES (:nom, :use, :em)"
        hojaSQL.execute(sql, nom=self.nombre, use=self.username, em=self.email)
        conexion.commit()
    
    @staticmethod
    def reiniciarTabla():
        sql = "TRUNCATE TABLE USUARIO"
        hojaSQL.execute(sql)
        sql2 = "ALTER TABLE USUARIO MODIFY(ID GENERATED AS IDENTITY (START WITH 1))"
        hojaSQL.execute(sql2)
    
    @staticmethod
    def obtenerTodos():
        sql = "SELECT * FROM USUARIO"
        hojaSQL.execute(sql)
        return hojaSQL.fetchall()