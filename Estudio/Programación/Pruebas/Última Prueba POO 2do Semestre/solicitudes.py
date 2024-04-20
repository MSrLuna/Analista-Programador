from tkinter import *
from tkinter.ttk import *
from libro import Libro


class SolicitudesVentana():
    def __init__(self, ventana2):
        ventana = ventana2
        ventana.geometry("1000x500")
        titulo = Label(ventana, text="Solicitudes de libros")
        titulo.pack()

        tabla = Treeview(ventana)
        tabla["columns"] = ["ID", "FECHA DE SOLICITUD", "TITULO", "NOMBRE", "APELLIDO" ]

        tabla.column(column="#0", width=5)
        tabla.column(column="ID", width=50)
        tabla.column(column="FECHA DE SOLICITUD", width=140)
        tabla.column(column="TITULO", width=150)
        tabla.column(column="NOMBRE", width=100)
        tabla.column(column="APELLIDO", width=100)
        

        tabla.heading(column="ID", text="ID")
        tabla.heading(column="FECHA DE SOLICITUD", text="FECHA DE SOLICITUD")
        tabla.heading(column="TITULO", text="TITULO")
        tabla.heading(column="NOMBRE", text="NOMBRE")
        tabla.heading(column="APELLIDO", text="APELLIDO")

        l = Libro()
        listaSolicitudes = l.historialSolicitudes()
        for l in listaSolicitudes:
            tabla.insert(parent="", index=END, value=l, iid=l[0])
        tabla.pack()