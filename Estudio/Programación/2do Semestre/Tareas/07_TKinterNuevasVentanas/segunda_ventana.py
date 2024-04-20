from tkinter import *

class SegundaVentana():
    # Creamos el constructor y pedimos que se nos pase por parámetro la ventana desde
    # la que vamos a crear esta segunda ventana
    def __init__(self, ventanaPadre):
        ventana = ventanaPadre
        ventana.geometry("500x500")
        texto = Label(ventana, text="HOLA, SOY LA SEGUNDA VENTANA")
        texto.pack()
    