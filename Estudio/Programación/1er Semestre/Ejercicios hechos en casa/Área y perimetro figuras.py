#Círculo
import math

radio = 3

area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio

print("Círculo:")
print("Área:", area)
print("Perímetro:", perimetro)

#Triángulo
base = 8
altura = 5
lado1 = 7
lado2 = 7
lado3 = 9

area = (base * altura) / 2
perimetro = lado1 + lado2 + lado3

print("Triángulo:")
print("Área:", area)
print("Perímetro:", perimetro)

#Cuadrado
lado = 5

area = lado ** 2
perimetro = 4 * lado

print("Cuadrado:")
print("Área:", area)
print("Perímetro:", perimetro)

#Trapezoide
base_mayor = 10
base_menor = 6
altura = 4
lado1 = 5
lado2 = 7

area = ((base_mayor + base_menor) * altura) / 2
perimetro = base_mayor + base_menor + lado1 + lado2

print("Trapezoide:")
print("Área:", area)
print("Perímetro:", perimetro)

#Rectangulo
base = 6
altura = 4

area = base * altura
perimetro = 2 * (base + altura)

print("Rectángulo:")
print("Área:", area)
print("Perímetro:", perimetro)

#Triangulo equilatero
import math

lado = 6

area = (math.sqrt(3) / 4) * (lado ** 2)
perimetro = 3 * lado

print("Triángulo Equilátero:")
print("Área:", area)
print("Perímetro:", perimetro)

#Polígono regular
import math

lado = 5  # longitud de cada lado
num_lados = 6  # número de lados

perimetro = lado * num_lados
apotema = lado / (2 * math.tan(math.pi / num_lados))
area = (perimetro * apotema) / 2

print("Polígono Regular:")
print("Área:", area)
print("Perímetro:", perimetro)

#Rectangulo con diagonal
import math

diagonal = 10
base = 6

altura = math.sqrt(diagonal ** 2 - base ** 2)
area = base * altura
perimetro = 2 * (base + altura)

print("Rectángulo con Diagonal:")
print("Área:", area)
print("Perímetro:", perimetro)

#Rombo
diagonal_mayor = 8
diagonal_menor = 6
lado = 5

area = (diagonal_mayor * diagonal_menor) / 2
perimetro = 4 * lado

print("Rombo:")
print("Área:", area)
print("Perímetro:", perimetro)

#Pentágono regular
import math

lado = 4

area = (5 * lado ** 2) / (4 * math.tan(math.pi / 5))
perimetro = 5 * lado

print("Pentágono Regular:")
print("Área:", area)
print("Perímetro:", perimetro)
