import random

def generar_rut():
    rut = random.randint(1000000, 99999999)
    digito_verificador = random.randint(0, 9)
    return f"{rut}-{digito_verificador}"

# Generar un RUT ficticio
rut_ficticio = generar_rut()
print("RUT Ficticio:", rut_ficticio)
