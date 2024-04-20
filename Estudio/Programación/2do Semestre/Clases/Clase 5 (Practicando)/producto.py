from conexion import hoja, conexion

class Producto:
    def __init__(self):
        self.id = None
        self.nombre = None
        self.precio = None
        self.stock = None
    
    #Este método mostrará cada fila que devuelve un SELECT a la BD.
    def Obtener_todos(self):
        sql = "SELECT * FROM producto"
        #recordemos que execute() no retorna valores, por eso no podemos guardar en un objeto hoja
        hoja.execute(sql)
        #Llamando a fetchall() extraemos los datos que quedaron guardados en el objeto hoja.
        #fetchall() retorna una lista de tuplas y lo dejamos guardado en resultado.
        resultado = hoja.fetchall()
        #if resultado está preguntando si ésta tiene valores dentro.
        if resultado:
            for fila in resultado:
                print(fila)
        else: #Si es que resultado no tiene valores.
            print("No hay productos registrados en la BD.")
            print()

    def Insertar(self):
        sql = "Insert into producto(nombre, precio, stock) values(:1, :2, :3)"

            #f...values('{self.nombre}', '{self.precio}', '{self.stock}') Es insegura esta forma de 
            #interpolaciones o concatenaciones, deja muy vulnerable SQL Injection.
        hoja.execute(sql, (self.nombre, self.precio, self.stock))
        #Hay que poner COMMIT para que no se pierdan los datos y haga ROLLBACK al terminar el programa.
        conexion.commit()