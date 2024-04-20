nombre = input("Ingrese nombre: ")
fono = input("Ingrese fono: ")
estadoCivil = input("Ingrese estado civil (S->Soltero, C->Casado, V->Viudo, D->Divorciado): ")

if estadoCivil == "S" or estadoCivil == "s":
    print("Soltero")
# elif es simplemente un if dentro de un else
elif estadoCivil == "C" or estadoCivil == "c":
    print("Casado")
elif estadoCivil == "V" or estadoCivil == "v":
    print("Viudo")
elif estadoCivil == "D" or estadoCivil == "d":
    print("Divorciado")


# Ejemplo de ELIF
# Este bloque IF ELSE IF es equivalente al que viene a continuación con ELIF
if 10 > 5:
    print("MAyor")
else:
    if 10 == 5:
        print("Iguales")

# Este bloque IF ELIF es equivalente al ejemplos anterior
if 10 > 5:
    print("Mayor")
elif 10 == 5:
    print("iguales")