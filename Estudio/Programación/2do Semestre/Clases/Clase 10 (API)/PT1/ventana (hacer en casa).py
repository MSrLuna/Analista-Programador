import requests
from tkinter import *
from tkinter.ttk import *

ventana = Tk()
ventana.title("Tabla cargada de datos USERS")
ventana.geometry("800x300")

url = "https://jsonplaceholder.typicode.com/users"
respuesta = requests.get(url)

json = []

if respuesta.status_code == 200:
    json = respuesta.json()

tabla = Treeview(ventana)
tabla["columns"] = ("ID", "NAME", "EMAIL", "PHONE", "WEBSITE")

tabla.column("#0", width=0)
tabla.column("ID", width=50)
tabla.column("NAME", width=50)
tabla.column("EMAIL", width=100)
tabla.column("PHONE", width=100)
tabla.column("WEBSITE", width=100)

tabla.heading(column="ID", text="Id")
tabla.heading(column="NAME", text="Nombre")
tabla.heading(column="EMAIL", text="Correo Electrónico")
tabla.heading(column="PHONE", text="Número telefónico")
tabla.heading(column="WEBSITE", text="Página Web")

for tarea in json:
    #Como values solo acepta lista/tupla para funcionar bien, entonces debemos crear una lista o tupla con la información del diccionario.
    #if de una sola línea.
    fila = [tarea["id"], tarea["name"], tarea["email"], tarea["phone"], tarea["website"]]
    tabla.insert(parent="", index=END, values=fila, iid=tarea["id"])

tabla.pack()
ventana.mainloop()