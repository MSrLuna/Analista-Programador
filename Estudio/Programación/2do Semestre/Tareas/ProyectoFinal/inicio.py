import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import requests
from insertar import InsetarVentana
from libro import Libro
from prestamo1 import PrestamoVentana
from socio import Socio
from solicitudes import SolicitudesVentana

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

ventana = tk.Tk()
ventana.title("Biblioteca")
ventana.geometry("650x250")
fuente = ("Tahoma", 18, "bold")

def solicitudes_libros():
    otraVentana = Toplevel(ventana)
    SolicitudesVentana(otraVentana)

def insertar_libro_socio():
    otraVentana = Toplevel(ventana)
    InsetarVentana(otraVentana)

def registrar_prestamo():
    otraVentana = Toplevel(ventana)
    PrestamoVentana(otraVentana)

def registrar_devolucion():
    pass

labelOpciones = Label(ventana, text="Opciones", font=fuente)
labelOpciones.pack(pady=10)

btnL = Button(ventana, text="Solicitudes de Libros", command=solicitudes_libros)
btnL.pack(expand=True, padx=10, pady=10)

btnI = Button(ventana, text="Insertar Libro o Socio", command=insertar_libro_socio)
btnI.pack(expand=True, padx=10, pady=10)

btnP = Button(ventana, text="Registrar Préstamo", command=registrar_prestamo)
btnP.pack(expand=True, padx=10, pady=10)

btnD = Button(ventana, text="Registrar Devolución", command=registrar_devolucion)
btnD.pack(expand=True, padx=10, pady=10)

ventana.mainloop()