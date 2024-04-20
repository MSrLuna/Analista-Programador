import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import requests
from libro import Libro
from socio import Socio
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Biblioteca")
ventana.geometry("650x650")
fuente = ("Tahoma", 18, "bold")
style1 = ttk.Style()
style1.configure("estilo1.TFrame", background="#17110E", foreground="white")
style2 = ttk.Style()
style2.configure("estilo2.TFrame", background="#491902", foreground="white")
style3 = ttk.Style()
style3.configure("TButton", background="#2C2B2B", foreground="white")
style4 = ttk.Style()
style4.configure("TLabel", background="#17110E", foreground='white', font=fuente)

frameIzq = ttk.Frame(ventana, width=150, height=650, style="estilo1.TFrame")
frameIzq.pack(side=tk.LEFT, padx=10, pady=10)
frameIzq.pack_propagate(False)

frameDer = ttk.Frame(ventana, width=500, height=650, style="estilo2.TFrame")
frameDer.pack(side=tk.RIGHT, padx=10, pady=10)
frameDer.pack_propagate(False)

def insertar_bd():
    messagebox.showinfo("Aviso", "Se han cargado las bases de datos de las url's.")

    url_socios = "http://45.236.130.191/api-prueba/biblioteca.php?action=socios"
    socios = requests.get(url_socios)
    if socios.status_code == 200:
        socios_json = socios.json()
        for l in socios_json:
            socioBD = Socio()
            socioBD.nombre = l["nombre"]
            socioBD.apellido = l["apellido"]
            socioBD.insertar()

    url_libros = "http://45.236.130.191/api-prueba/biblioteca.php?action=libros"
    libros = requests.get(url_libros)
    if libros.status_code == 200:
        libros_json = libros.json()
        for l in libros_json:
            libroBD = Libro()
            libroBD.titulo = l["titulo"]
            libroBD.disponible = l["disponible"]
            libroBD.insertar()

def formateo():
    l = Libro()
    s = Socio()
    l.eliminar()
    s.eliminar()

def limpiar_frame_der():
    for widget in frameDer.winfo_children():
        widget.destroy()

def libros():

    limpiar_frame_der()

    tabla = Treeview(frameDer, style="estilo2.TFrame")
    tabla["columns"] = ["ID", "TITULO", "DISPONIBLE"]

    tabla.column(column="#0", width=5)
    tabla.column(column="ID", width=50)

    tabla.heading(column="ID", text="ID")
    tabla.heading(column="TITULO", text="TITULO")
    tabla.heading(column="DISPONIBLE", text="DISPONIBLE")

    listaLibros = Libro.obtenerLibros()
    for l in listaLibros:
        tabla.insert("", END, values=l, iid=l[0])
    tabla.pack()

def insertar_libro_socio():

    limpiar_frame_der()

    titulo = Label(frameDer, text="Ingresar Libro")
    titulo.pack()
    space2 = Label(frameDer, text="")
    space2.pack()

    tituloLabel = Label(frameDer,text="Titulo")
    tituloEntry = Entry(frameDer, )
    tituloLabel.pack()
    tituloEntry.pack()

    disponibleLabel = Label(frameDer, text="Disponible")
    disponibleEntry = Entry(frameDer, )
    disponibleLabel.pack()
    disponibleEntry.pack()

    space4= Label(frameDer,text="")
    space4.pack()

    def ingresarLibro():
        libro = Libro()
        libro.titulo = tituloEntry.get()
        libro.disponible = disponibleEntry.get()

        libro.insertar()

    buttonEnterLibro = Button(frameDer, text="Ingresar Libro",command=ingresarLibro)
    buttonEnterLibro.pack()

    space59= Label(frameDer,text="")
    space59.pack()

    titulo = Label(frameDer, text="Ingresar Socio")
    titulo.pack()
    space2 = Label(frameDer, text="")
    space2.pack()

    nombreLabel = Label(frameDer,text="Nombre")
    nombreEntry = Entry(frameDer, )
    nombreLabel.pack()
    nombreEntry.pack()

    apellidoLabel = Label(frameDer, text="Apellido")
    apellidoEntry = Entry(frameDer, )
    apellidoLabel.pack()
    apellidoEntry.pack()

    space4= Label(frameDer,text="")
    space4.pack()

    def ingresarSocio():
        socio = Socio()
        socio.nombre = nombreEntry.get()
        socio.apellido = apellidoEntry.get()

        socio.insertar()

    buttonEnterSocio = Button(frameDer, text="Ingresar Socio",command=ingresarSocio)
    buttonEnterSocio.pack()






def prestamos():
    
    limpiar_frame_der()

    titulo = Label(frameDer, text="Solicitudes de libros")
    titulo.pack()
    
    tabla = Treeview(frameDer, style="estilo2.TFrame")
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

labelOpciones = Label(frameIzq, text="Opciones", font=fuente, style="TLabel")
labelOpciones.pack(pady=10)

boton_config = {'background': '#2C2B2B', 'foreground': 'white', 'padx': 10, 'pady': 10, 'relief': tk.FLAT}

btnU= tk.Button(frameIzq, text="Insertar URL's", command=insertar_bd, **boton_config)
btnU.pack(expand=True)

btnF = tk.Button(frameIzq, text="Eliminar contenido BD", command=formateo, **boton_config)
btnF.pack(expand=True)

btnL = tk.Button(frameIzq, text="Libros", command=libros, **boton_config)
btnL.pack(expand=True)

btnI = tk.Button(frameIzq, text="Insertar Libro o Socio", command=insertar_libro_socio, **boton_config)
btnI.pack(expand=True)

btnP = tk.Button(frameIzq, text="Prestamos", command=prestamos, **boton_config)
btnP.pack(expand=True)

ventana.mainloop()