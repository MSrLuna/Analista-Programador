def calculadora(num1, num2):
    print("Seleccione ejercicio a realizar:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. División")
    print("5. Raíz (solo primer número)")
    opción = int(input("Opción: "))
    if opción == 1:
        s = num1 + num2
        print("Resutado suma:", s)
    elif opción == 2:
        r = num1 - num2
        print("Resultado resta:", r)
    elif opción == 3:
        m = num1 * num2
        print("Resultado Multiplicación:", m)
    elif opción == 4:
        d = num1 / num2
        print("Resultado división:", d)
    elif opción == 5:
        ra = num1 * 0.5
        print("Resultado raíz cuadrada:", ra)
    else:
        print("Opcón no existente.")

n1 = float(input("Primer número:  |  "))
n2 = float(input("Segundo número: |  "))

calculadora(n1, n2)