#Ingresar los datos nombres, apellido de un curso de 25. Luego visualizar la cantidad de nombres “maría” y “Jose” existentes en el curso.

curso = []
contador_maria = 0
contador_jose = 0

for i in range(25):
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    curso.append([nombre, apellido])
    
for estudiante in curso:
    if estudiante[0] == "María":
        contador_maria += 1
    elif estudiante[0] == "José":
        contador_jose += 1

print("Cantidad de nombres María:", contador_maria)
print("Cantidad de nombres José:", contador_jose)