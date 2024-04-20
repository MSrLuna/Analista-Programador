import time

def imprimir_cada_0_5_segundos(numero_veces):
    for i in range(numero_veces):
        print()
        time.sleep(0.1)

imprimir_cada_0_5_segundos(40)

print("██████╗░██╗███████╗███╗░░██╗██╗░░░██╗███████╗███╗░░██╗██╗██████╗░░█████╗░")
print("██╔══██╗██║██╔════╝████╗░██║██║░░░██║██╔════╝████╗░██║██║██╔══██╗██╔══██╗")
print("██████╦╝██║█████╗░░██╔██╗██║╚██╗░██╔╝█████╗░░██╔██╗██║██║██║░░██║██║░░██║")
print("██╔══██╗██║██╔══╝░░██║╚████║░╚████╔╝░██╔══╝░░██║╚████║██║██║░░██║██║░░██║")
print("██████╦╝██║███████╗██║░╚███║░░╚██╔╝░░███████╗██║░╚███║██║██████╔╝╚█████╔╝")
print("╚═════╝░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═╝╚═════╝░░╚════╝░")

imprimir_cada_0_5_segundos(40)

contador = True

while contador:
    try:
        print("Ingrese los datos sin puntos (a menos de que sean decimales) ni comas.")
        print()
        print("Ingrese sueldo mensual.")
        print()
        sueldo = float(input("( ͡❛ ͜ʖ ͡❛) 👉 "))
        print()
        print("Ingrese el porcentaje que desee ahorrar y/o dedicar a alguna inversión.")
        print()
        porcentaje = float(input("( ͡❛ ͜ʖ ͡❛) 👉 "))
        sueldop = (porcentaje/100)*sueldo
        print()
        print("Del porcentaje dedicado a ahorro y/o inversiones qué porcentaje desea desea dedicar a las siguientes actividades.")
        print()
        ahorrop = float(input("Dedicado a ahorro. (👍 °︡ ︹ °︠ )👍 "))
        dólaresp = float(input("Dedicado a dolarizar. (👍 ◉︡ ︹ ◉︠ )👍 "))
        inversiónp = float(input("Dedicado a inversiones. (👍 ⊙︡ ︹ ⊙︠ )👍 "))
        ahorro = (ahorrop/100)*sueldop
        dólares = (dólaresp/100)*sueldop
        inversión = (inversiónp/100)*sueldop
        print()
        print("Ingrese valor actual del dólar(USD) en peso chileno(CLP).")
        dólar_actual = float(input("(◡̃ ﹏◡̃) 👉 "))
        contador = False
    except:
        print()
        print("¡¡Tienen que ser valores numericos, no texto!! (╯ ◣︡ ︹ ◢︠ )╯┻━┻")
        print()
        continue

contador2 = True

while contador2:
    try:
        print()
        print("Ahora teniendo los datos decida que desea hacer. 【 ͡ᵔ ͜ʖ ͡ᵔ】")
        print()
        print("1. Ver gastos.")
        print("2. Calcular ganancia en meses (ahorros).")
        print("3. Salir.")
        print()
        opción_seleccionada_1 = int(input("¿( o︡ . O︠ )? "))
        print()
    except:
        print()
        print("¡¡Tienen que ser valores numericos enteros dentro de las opciones!! (╯ ◣︡ ︹ ◢︠ )╯┻━┻")
        print()
        continue
    if opción_seleccionada_1 == 1:
        dolarizado = dólares/dólar_actual
        print(f"Total dejado en ahorro (ノ 🔥︡ ▭ 🔥︠ )ノ ${ahorro}.")
        print(f"Total gastado en dólares (ノ 🔥︡ ▭ 🔥︠ )ノ ${dólares} (${dolarizado} (tomando en cuenta el valor actual)).")
        print(f"Total gastado en inversiones (ノ 🔥︡ ▭ 🔥︠ )ノ ${inversión}.")
    elif opción_seleccionada_1 == 2:
        cuentas=[]
        print("Agregue la cantidad de cuentas ahorro tiene.")
        print()
        contador3 = int(input("( ͡❛ ͜ʖ ͡❛)👌 "))
        print()
        for cuenta in range(1, contador3 + 1):
            porcentaje_ganancia = float(input(f"Ingresa el porcentaje de ganancia para la cuenta {cuenta} (sin símbolo %): "))
            cuentas.append(porcentaje_ganancia)
        print("Ingrese por cuántos meses desea calcular las ganancias.")
        print()
        meses = int(input("( ͡❛ ͜ʖ ͡❛)👌 "))
        print()
        sueldo_actual = sueldo
        for mes in range(1, meses + 1):
            for cuenta, porcentaje in enumerate(cuentas, start=1):
                crecimiento_cuenta = (1 + porcentaje / 100) ** mes
                sueldo_actual *= crecimiento_cuenta
                print(f"\nMes {mes} - Cuenta de ahorro {cuenta}:")
                print(f"Sueldo actual: {sueldo_actual:.2f}")