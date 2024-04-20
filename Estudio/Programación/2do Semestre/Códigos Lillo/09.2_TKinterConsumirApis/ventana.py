import requests
from tkinter import *
from tkinter.ttk import *

ventana = Tk()
ventana.title("Tabla cargada desde ApiREST")
ventana.geometry("800x500")

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

tabla.heading(column="USERID", text="ID Usuario")
tabla.heading(column="ID", text="ID Tarea")
tabla.heading(column="TITULO", text="Tarea")
tabla.heading(column="ESTADO", text="Estado")

for tarea in json:
    # if tarea["completed"]:
    #     estado = "Completada"
    # else:
    #     estado = "No realizada"

    # expresión ternaria: es un IF corto, un IF de una sola línea
    # primero asigno el valor si IF es cierto
    # segundo, pongo la condición IF
    # tercero, pongo el bloque ELSE y lo que debe asignar a estado cuando IF sea falso
    estado = "Completada" if tarea["completed"] else "No realizada"
    # como values solo acepta una lista o una tupla para funcionar bien.. entonces
    # tenemos que crear una lista o tupla con la información del diccionario
    fila = [tarea["userId"], tarea["id"], tarea["title"], estado]
    tabla.insert(parent="", index=END, values=fila, iid=tarea["id"])

tabla.pack()

ventana.mainloop()