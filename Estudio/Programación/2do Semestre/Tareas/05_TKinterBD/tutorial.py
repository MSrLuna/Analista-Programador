from tkinter import *
from tkinter import font

# Con esta simple línea creamos una ventana en el SO Windows
ventana = Tk()
# A partir de la instancia (objeto) que creamos de la clase Tk, podremos llamar
# a distintos métodos para modificar su apariencia..
# Por ejemplo, podemos especificar el ancho y alto que tendrá la ventana
ventana.geometry("500x500")
# Si llamamos al método .title() 
# podremos modificar el título de la ventana, entregándole un string con el texto
ventana.title("Mi primer TKinter")

# podemos dejar en una variable los estilos de fuentes
# 1. Familia de fuentes
# 2. Tamaño de las letras
# 3. Ancho de los caracteres.. bold, normal..
fuentes = ("Comic Sans MS", 18, "bold")

# El primer param que le pasamos a Label tiene que ser el objeto de la clase Tk
# Después, podemos modificar los parámetros que queramos..
labelNombre = Label(ventana, text="Nombre", font=fuentes)
# Con pack() posicionamos el elemento dentro de la ventana
labelNombre.pack()

txtNombre = Entry(ventana, font=fuentes)
txtNombre.pack()

labelApellido = Label(ventana, text="Apellido", font=fuentes)
labelApellido.pack()
txtApellido = Entry(ventana, font=fuentes)
txtApellido.pack()

labelEdad = Label(ventana, text="Edad", font=fuentes)
labelEdad.pack()
txtEdad = Entry(ventana, font=fuentes)
txtEdad.pack()

def saludar():
    # El método .get() de un objeto Entry, obtiene lo que se escribió en la caja de texto
    nombre = txtNombre.get()
    ape = txtApellido.get()
    e = txtEdad.get()
    # print(f"Hola {nombre} {ape}. Tu edad es de {e} años")
    # Mostrar este mismo mensaje, pero MODIFICANDO un Label
    mensaje = f"Hola {nombre} {ape}. Tu edad es de {e} años"
    # Cómo modifico el texto de un Label??
    # Pensando en Label como si fuera un diccionario al que accederemos a su propiedad text
    labelSaludo["text"] = mensaje

# en la propiedad command ponemos el nombre de un método PERO SIN SUS PARÉNTESIS!
# Ese método tiene que estar creado ANTES de la creación del botón
boton = Button(ventana, text="Saludar!", font=fuentes, bg="blue", fg="white",
               command=saludar)
boton.pack()

labelSaludo = Label(ventana, text="Aquí va el saludo...", font=fuentes)
labelSaludo.pack()

# Al final de todo el código SIEMPRE pondremos la siguiente línea
ventana.mainloop()