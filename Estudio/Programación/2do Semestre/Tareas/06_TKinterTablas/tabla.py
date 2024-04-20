from tkinter import *
from tkinter.ttk import *

ventana = Tk()
ventana.geometry("1000x500")
ventana.title("Tablas con datos en duro")
# PASO 1: crear la tabla e indicarle que se muestre dentro de ventana
tabla = Treeview(ventana)
# PASO 2: en una TUPLA, agregar los identificadores para cada Columna..
# En este punto creamos los encabezados, PERO NO SON VISIBLES.. solo sirven para identificar
tabla["columns"] = ("ID", "NOMBRE", "APELLIDO", "EDAD")

# PASO 2.5 (opcional): puedes dar estilos a las columnas llamando al método column
# El identificador para la primera columna que pone TKinter por defecto es "#0"
tabla.column(column="#0", width=0)
tabla.column(column="ID", width=50)
tabla.column(column="EDAD", width=50)

# PASO 3: les damos un TEXTO a los ENCABEZADOS
tabla.heading(column="APELLIDO", text="Apellido")
tabla.heading(column="ID", text="ID")
tabla.heading(column="EDAD", text="Edad")
tabla.heading(column="NOMBRE", text="Nombre")

# PASO 4: obtener las tuplas de datos que se insertarán en la tabla
tupla1 = (100, "Brandon", "Oliva", 20)
tupla2 = (200, "Gabriel", "Acum", 21)
tupla3 = (300, "Franco", "Luna", 17)
tupla4 = (400, "Francisco", "Pinol 2.0", 23)

# PASO 5: INSERTAR las tuplas dentro de la TABLA
# parent: indica si esta fila es una subfila de otra fila (dejar siempre "")
# index: la posición donde agregaremos la fila que estamos insertando.. si queremos
# el funcionamiento típico (insertar después de la última fila), pondremos END
# values: aquí va la TUPLA de datos que se insertarán
# iid: identificador de cada FILA.. debe ser ÚNICO por cada tabla
tabla.insert(parent="", index=END, values=tupla1, iid="0")
tabla.insert(parent="", index=END, values=tupla2, iid="1")
tabla.insert(parent="", index=END, values=tupla3, iid="2")
tabla.insert(parent="", index=END, values=tupla4, iid="3")

tabla.pack()

ventana.mainloop()