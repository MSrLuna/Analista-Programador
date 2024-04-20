texto = "Hola, mundo!"

# Cambiar mayúsculas y minúsculas
print(texto.lower())      # hola, mundo!
print(texto.upper())      # HOLA, MUNDO!
print(texto.capitalize()) # Hola, mundo!
print(texto.title())      # Hola, Mundo!

# Reemplazar texto
print(texto.replace("Hola", "Adiós"))  # Adiós, mundo!

# Dividir y combinar texto
palabras = texto.split(", ")  
print(palabras)              # ['Hola', 'mundo!']
nuevo_texto = "-".join(palabras)
print(nuevo_texto)           # Hola-mundo!

# Eliminar espacios en blanco
espacios = "   hola   "
print(espacios.strip())      # hola

# Obtener longitud y contar caracteres
print(len(texto))            # 12
print(texto.count("o"))      # 2

texto = "Hola, mundo!"

# Obtener subcadenas
print(texto[0:4])       # Hola
print(texto[6:])        # mundo!

# Verificar el inicio y el final de un texto
print(texto.startswith("Hola"))     # True
print(texto.endswith("mundo!"))     # True

# Dividir el texto en líneas
texto_multilinea = "Hola\nMundo!"
lineas = texto_multilinea.splitlines()
print(lineas)          # ['Hola', 'Mundo!']

# Formatear texto
nombre = "Juan"
edad = 25
saludo = "Hola, mi nombre es {} y tengo {} años.".format(nombre, edad)
print(saludo)          # Hola, mi nombre es Juan y tengo 25 años.

# Verificar si un carácter o subcadena está presente
print("mundo" in texto)     # True
print("adiós" in texto)     # False

texto = "Hola, ¿cómo estás?"

# Dividir el texto en palabras
palabras = texto.split()
print(palabras)         # ['Hola,', '¿cómo', 'estás?']

# Alinear el texto
print(texto.ljust(20))  # Hola, ¿cómo estás?   
print(texto.rjust(20))  #   Hola, ¿cómo estás? 
print(texto.center(20)) # Hola, ¿cómo estás?  

# Verificar el tipo de carácter
print(texto.isalpha())   # False
print(texto.isdigit())   # False
print(texto.isalnum())   # False
print(texto.isspace())   # False

# Partir el texto en párrafos
texto_largo = "Este es el primer párrafo.\n\nEste es el segundo párrafo."
parrafos = texto_largo.split('\n\n')
print(parrafos)         # ['Este es el primer párrafo.', 'Este es el segundo párrafo.']
