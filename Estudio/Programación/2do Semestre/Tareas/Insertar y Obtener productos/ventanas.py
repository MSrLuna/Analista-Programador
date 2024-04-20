from tkinter import *
from tkinter.ttk import *
from producto import Producto

class InsertarP:
    def __init__(self, VentanaPadre):
        ventana = VentanaPadre
        ventana.geometry("360x300")
        ventana.title("Insertar datos en la tabla 'Producto'")
        estiloFuentes = ("Tahoma", 18, "bold")

        labelNombre = Label(ventana, text="Nombre", font=estiloFuentes)
        labelNombre.pack()
        txtNombre = Entry(ventana, font=estiloFuentes)
        txtNombre.pack()

        labelPrecio = Label(ventana, text="Precio", font=estiloFuentes)
        labelPrecio.pack()
        txtPrecio = Entry(ventana, font=estiloFuentes)
        txtPrecio.pack()

        labelStock = Label(ventana, text="Stock", font=estiloFuentes)
        labelStock.pack()
        txtStock = Entry(ventana, font=estiloFuentes)
        txtStock.pack()

        def insertarProducto():

            p = Producto()
            p.nombre = txtNombre.get()
            p.precio=  txtPrecio.get()
            p.stock = txtStock.get()
            p.insertar()

        btnInsertar = Button(ventana, text="Guardar", font=estiloFuentes,
                            bg="blue", fg="white", command=insertarProducto)
        btnInsertar.pack()

class ObtenerP:
    def __init__(self, VentanaPadre):
        ventana = VentanaPadre
        ventana.geometry("550x250")
        ventana.title("Datos en la tabla 'Producto'")

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
        filas = p.obtenerDatos()

        for tupla in filas:
            tabla.insert(parent="", index=END, values=tupla, iid=tupla[0])

        tabla.pack()

