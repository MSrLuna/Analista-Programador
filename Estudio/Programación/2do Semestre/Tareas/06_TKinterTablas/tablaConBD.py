from tkinter import *
from tkinter.ttk import *
from producto import *

ventana = Tk()
ventana.geometry("1000x500")
ventana.title("Tabla con datos de la BD")

tabla = Treeview(ventana)
tabla["columns"] = ("ID", "NOMBRE", "PRECIO", "STOCK")

tabla.column(column="#0", width=50)
tabla.column(column="ID", width=80)
tabla.column(column="PRECIO", width=100)
tabla.column(column="STOCK", width=100)

tabla.heading(column="ID", text="ID")
tabla.heading(column="NOMBRE", text="Nombre")
tabla.heading(column="PRECIO", text="Precio")
tabla.heading(column="STOCK", text="Stock")

p = Producto()
# obtenerDatos() devuelve el fetchall() del SELECT que se ejecutó
# RECORDEMOS que fetchall() retorna una LISTA de TUPLAS
filas = p.obtenerDatos()
# Como filas es una LISTA.. la recorremos
for tupla in filas:
    # tupla absorbe una TUPLA por cada recorrido de la LISTA filas
    # tupla[0] está accediendo a la columna ID de la tabla producto
    tabla.insert(parent="", index=END, values=tupla, iid=tupla[0])

tabla.pack()
ventana.mainloop()