switch = True
while switch:
    try:
        n1 = int(input("ingrese nota 1: "))
        n2 = int(input("ingrese nota 2: "))
        n3 = int(input("ingrese nota 3: "))
    except:
        print("Solo números.")
        print("Vuelve a intentarlo.")