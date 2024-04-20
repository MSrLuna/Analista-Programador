import requests
from usuario import Usuario
from tkinter import *
from tkinter.ttk import *

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        # Este es un método STATIC, por lo que NO NECESITA un objeto para ser llamado
        # Simplemente, ponemos el nombre de la clase donde está, y hacer .metodo()
        Usuario.reiniciarTabla()
        usuarios = respuesta.json()
        for u in usuarios:
            usuarioBD = Usuario()
            usuarioBD.nombre = u["name"]
            usuarioBD.username = u["username"]
            usuarioBD.email = u["email"]
            usuarioBD.insertar()

    ventana = Tk()
    ventana.geometry("800x500")

    tabla = Treeview(ventana)
    tabla["columns"] = ("ID", "NOMBRE", "USERNAME", "EMAIL")
    tabla.column(column="#0", width=0)
    tabla.column(column="ID", width=50)
    
    tabla.heading(column="ID", text="ID")
    tabla.heading(column="NOMBRE", text="NOMBRE")
    tabla.heading(column="USERNAME", text="USERNAME")
    tabla.heading(column="EMAIL", text="EMAIL")

    listaUsuarios = Usuario.obtenerTodos()
    for fila in listaUsuarios:
        tabla.insert("", END, values=fila, iid=fila[0])
    
    tabla.pack()
    
    ventana.mainloop()