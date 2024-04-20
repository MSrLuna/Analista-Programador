# Escritura en un archivo
with open("archivo.txt", "w") as archivo:
    archivo.write("Hola, archivo!")

# Lectura de un archivo
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

#La gestión de archivos se realiza mediante el uso de las funciones open() y close().
#El uso de with garantiza que el archivo se cierre automáticamente después de su uso.
#write() se utiliza para escribir en un archivo, mientras que read() se utiliza para leer el contenido del archivo.
#Espero que estos ejemplos detallados te ayuden a comprender mejor la sintaxis y las estructuras básicas en Python.