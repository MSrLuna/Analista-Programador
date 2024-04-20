from tkinter import *

#Con esta simple línea cramos una ventana en SO Windows.
ventana = Tk()

#Con esto podremos especificar el ancho y alto de la ventana (sin con margenes que tienen todas lasventanas por defecto).
ventana.geometry("600x300")

#Si llamamos al método .title() podremos modificar el título de la ventana.
ventana.title("Mi primer TKinter")

#Podemos guardar las fuentes en variables:
#1. Familia de fuentes.
#2. Tamaño de las letras.
#3. Ancho de los carácteres.. bold, normal..
fuentes=("Comic Sans MS", 18, "bold", "italic")

#El primer parámetro que le pasamos a Label tiene que ser el objeto de la clase Tk.
#Después podemos modificar los parámetros que queramos.
labelNombre = Label(ventana, text="Nombre", font=fuentes)

#Con pack() llamamos al elemento dentro de la ventana.
labelNombre.pack()

#Es como poner un input dentro de la ventana.
txtNombre = Entry(ventana, font=("Segoe UI", 10, "italic"))
txtNombre.pack()

labelApellido = Label(ventana, text="Apellido", font=fuentes)
labelApellido.pack()

txtApellido = Entry(ventana, font=("Segoe UI", 10, "italic"))
txtApellido.pack()

labelEdad = Label(ventana, text="Edad", font=fuentes)
labelEdad.pack()

txtEdad = Entry(ventana, font=("Segoe UI", 10, "italic"))
txtEdad.pack()

#Crear un botón.
#bg es el color del botón antes de ser presionado y el fg mientrás está presionado.
#command hace referencia a una función, en este caso a saludar.
def saludar():
    #El método .get() de un objeto Entry, obtiene lo que se escribió en la caja de texto.
    nombre = txtNombre.get()
    apellido = txtApellido.get()
    edad = txtEdad.get()
    #print(f"Hola {nombre} {apellido} cuya edad es de {edad} años.")
    #Mostrar este mismo mensaje, pero modificando un Label
    mensaje = f"Hola {nombre} {apellido} cuya edad es de {edad} años."
    #¿Cómo modifico el texto de un Label?
    #Pensando en Label como si fuera un diccionario al que accederemos a su propiedad
    labelSaludo["text"] = mensaje
boton = Button(ventana, text="Saludar", font=("Segoe UI", 15, "bold"), bg="blue", fg="white", command=saludar)
boton.pack()

labelSaludo = Label(ventana, text="<Texto>", font=fuentes)
labelSaludo.pack()

#Al final de todo el código SIEMPRE pondremos la siguiente línea.
ventana.mainloop()