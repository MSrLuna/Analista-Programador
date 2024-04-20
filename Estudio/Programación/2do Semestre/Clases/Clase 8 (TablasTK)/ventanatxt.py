from tkinter import *

class SegundaVentana():

    def __init__(self, ventanaPadre):
        ventana = ventanaPadre
        texto = Label(ventana, text="Hola, soy la segunda ventana")
        texto.pack()

        ventana.mainloop()