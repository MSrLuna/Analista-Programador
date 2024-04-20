import sqlite3

# Conexión a la base de datos
conexion = sqlite3.connect('basedatos.db')
cursor = conexion.cursor()

# Creación de una tabla
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    email TEXT NOT NULL,
                    edad INTEGER)''')
conexion.commit()

# Inserción de datos en la tabla
nombre = input("Ingrese el nombre del usuario: ")
email = input("Ingrese el email del usuario: ")
edad = int(input("Ingrese la edad del usuario: "))

cursor.execute("INSERT INTO usuarios (nombre, email, edad) VALUES (?, ?, ?)", (nombre, email, edad))
conexion.commit()

# Consulta de datos en la tabla
cursor.execute("SELECT * FROM usuarios")
resultados = cursor.fetchall()
for fila in resultados:
    print(f"ID: {fila[0]}")
    print(f"Nombre: {fila[1]}")
    print(f"Email: {fila[2]}")
    print(f"Edad: {fila[3]}")
    print("------------------")

# Actualización de datos en la tabla
id_usuario = int(input("Ingrese el ID del usuario a actualizar: "))
nueva_edad = int(input("Ingrese la nueva edad del usuario: "))

cursor.execute("UPDATE usuarios SET edad = ? WHERE id = ?", (nueva_edad, id_usuario))
conexion.commit()

# Eliminación de datos en la tabla
id_usuario = int(input("Ingrese el ID del usuario a eliminar: "))

cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
conexion.commit()

# Cierre de la conexión a la base de datos
conexion.close()
