from tkinter import * 
import requests

ventana = Tk()
ventana.geometry("1024x768")

api = requests.get("http://45.236.130.191/api-prueba/datos.php?action=ciudades")
if api.status_code == 200:
    json = api.json()
    lista = []
    for i in json:
        lista.append(i["nombre"])
    options = StringVar()
    eleccion = OptionMenu(ventana, options, *lista)
    eleccion.pack()

ventana.mainloop()