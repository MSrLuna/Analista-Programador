#Ingresar los datos nombres, apellido y sexo de un curso de 35. Luego visualizar la cantidad de hombres, mujeres existentes en el curso. 

curso = []
contador_hombres = 0
contador_mujeres = 0

for i in range(35):
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    sexo = input("Ingrese el sexo del estudiante (M/F): ")
    curso.append([nombre, apellido, sexo])
    
for estudiante in curso:
    if estudiante[2] == "M":
        contador_hombres += 1
    elif estudiante[2] == "F":
        contador_mujeres += 1

print("Cantidad de hombres:", contador_hombres)
print("Cantidad de mujeres:", contador_mujeres)