def netoiva(total):
    iva_actual = 0.19
    iva = total * iva_actual
    neto = total - iva
    print("Neto:          $", neto)
    print("Iva:           $", iva)

n1 = float(input("Total pagado:  $ "))

netoiva(n1)