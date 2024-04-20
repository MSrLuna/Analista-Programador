import requests
from tkinter import *
from tkinter.ttk import *

ventana = Tk()
ventana.title("Tabla cargada desde ApiREST")
ventana.geometry("800x250")

url = "https://jsonplaceholder.typicode.com/todos"
respuesta = requests.get(url)

json = []

if respuesta.status_code == 200:
    json = respuesta.json()

tabla = Treeview(ventana)
tabla["columns"] = ("USERID", "ID", "TITULO", "ESTADO")

tabla.column("#0", width=0)
tabla.column("USERID", width=50)
tabla.column("ID", width=50)
tabla.column("TITULO", width=450)

tabla.heading(column="USERID", text="Id Usuario")
tabla.heading(column="ID", text="Id Tarea")
tabla.heading(column="TITULO", text="Tarea")
tabla.heading(column="ESTADO", text="Estado")

for tarea in json:
    #Como values solo acepta lista/tupla para funcionar bien, entonces debemos crear una lista o tupla con la información del diccionario.
    #if de una sola línea.
    estado = "Completada" if tarea["completed"] else "No realizada"
    fila = [tarea["userId"], tarea["id"], tarea["title"], estado]
    tabla.insert(parent="", index=END, values=fila, iid=tarea["id"])

tabla.pack()
ventana.mainloop()