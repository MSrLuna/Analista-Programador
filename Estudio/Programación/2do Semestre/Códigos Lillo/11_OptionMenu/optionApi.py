from tkinter import *
import requests

ventana = Tk()
ventana.geometry("500x500")

url = "http://45.236.130.191/api-prueba/datos.php?action=ciudades"
respuesta = requests.get(url)
if respuesta.status_code == 200:
    ciudades = respuesta.json()
    ciudadSeleccionada = StringVar()

    listaOpciones = []
    for c in ciudades:
        listaOpciones.append(c["nombre"])
        
    menuCiudades = OptionMenu(ventana, ciudadSeleccionada, *listaOpciones)
    menuCiudades.pack()

ventana.mainloop()