from tkinter import *
from menu import VentanaMenu

ventana = Tk()
ventana.title("Login")
ventana.geometry("500x500")
fuentes = ("Segoe UI", 18, "bold")

txtUsuario = Entry(ventana, font=fuentes)
txtUsuario.pack()
txtPassword = Entry(ventana, font=fuentes)
txtPassword.pack()

usuario = txtUsuario
contrasena = txtPassword

def iniciarSesion():
    if txtUsuario.get() == "INACAP" and txtPassword.get() == "1234":
        ventanaMenu = Toplevel(ventana)
        VentanaMenu(ventanaMenu)
    else:
        ventanaError = Tk()
        ventanaError.title("ERROR")
        ventanaError.geometry("250x50")
        labelError = Label(ventanaError, text="Error, Usuario o contraseña no válidos.")
        labelError.pack()

btnLogin = Button(ventana, text="Iniciar Sesión", bg="blue", fg="white", command=iniciarSesion, font=fuentes)
btnLogin.pack()

ventana.mainloop()