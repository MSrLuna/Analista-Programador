from tkinter import *
from tkinter.ttk import *
from producto import Producto
from actualizar import VentanaActualizarProducto

class VentanaListarProductos:
    def __init__(self, ventana):
        ventana.geometry("1000x500")
        ventana.title("Tabla con datos de la BD")

        tabla = Treeview(ventana)
        tabla["columns"] = ("ID", "NOMBRE", "PRECIO", "STOCK")

        tabla.column(column="#0", width=50)
        tabla.column(column="ID", width=80)
        tabla.column(column="NOMBRE", width=250)
        tabla.column(column="PRECIO", width=100)
        tabla.column(column="STOCK", width=100)

        tabla.heading(column="ID", text="ID")
        tabla.heading(column="NOMBRE", text="Nombre")
        tabla.heading(column="PRECIO", text="Precio")
        tabla.heading(column="STOCK", text="Stock")

        p = Producto()
        filas = p.obtenerDatos()
        for tupla in filas:
            tabla.insert(parent="", index=END, values=tupla, iid=tupla[0])
        
        def onClick(event):
            iid = tabla.selection()[0]
            ventanaActualizar = Toplevel(ventana)
            VentanaActualizarProducto(ventanaActualizar, iid)
        tabla.bind("<ButtonRelease-1>", onClick)
        tabla.pack()
