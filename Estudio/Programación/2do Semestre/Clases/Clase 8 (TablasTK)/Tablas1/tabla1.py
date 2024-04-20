from tkinter import *
from tkinter.ttk import *
from producto import *

ventana = Tk()
ventana.geometry("1240x768")
ventana.title = ("Ejemplo")
tabla = Treeview(ventana)
tabla["columns"] = ("ID", "NOMBRE", "PRECIO", "STOCK")

tabla.column(column="ID", width=50)
tabla.column(column="#0", width=50)
tabla.column(column="STOCK", width=50)
tabla.column(column="PRECIO", width=100)

tabla.heading(column="#0", text="#")
tabla.heading(column="ID", text="ID")
tabla.heading(column="NOMBRE", text="Nombre")
tabla.heading(column="PRECIO", text="Precio")
tabla.heading(column="STOCK", text="Stock")

p = Producto()
filas = p.obtenerDatos()

for tupla in filas:
    tabla.insert(parent="", index=END, values=tupla, iid=tupla[0])

tabla.pack()
ventana.mainloop()