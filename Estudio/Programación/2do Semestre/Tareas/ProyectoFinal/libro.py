from conexion import conexion, hoja

class Libro:
    def __init__(self):
        self.id = None
        self.titulo = None
        self.disponible = None
    
    def insertar(self):
        sql = "INSERT INTO libro (titulo, disponible) VALUES (:tit, :dis)"
        hoja.execute (sql, tit=self.titulo, dis=self.disponible)
        conexion.commit()

    @staticmethod
    def historialSolicitudes():
        sql = "SELECT solicitud.id, fecha_solicitud, titulo, nombre, apellido FROM solicitud INNER JOIN libro ON libro.id = solicitud.id_libro INNER JOIN socio ON socio.id = solicitud.id_socio"
        hoja.execute(sql)
        return hoja.fetchall()  
    
    @staticmethod
    def reiniciarTabla():
        sql = "TRUNCATE TABLE libro"
        hoja.execute(sql)
        sql2 = "ALTER TABLE libro MODIFY(ID GENERATED AS IDENTITY (START WITH 1))"
        hoja.execute(sql2)

    @staticmethod
    def obtenerLibros():
        sql = "SELECT id, titulo, disponible FROM libro"
        hoja.execute(sql)
        return hoja.fetchall()
    
    def prestamo(self):
        sql = "SELECT titulo FROM libro"
        hoja.execute(sql)
        return hoja.fetchall()

    def devolver(self):
        pass