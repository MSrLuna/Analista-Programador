from conexion import hoja

print()
print("Seleccione tabla a consultar:")
print()
contador = True
while contador:
        print("1. Empleados.")
        print("2. Trabajos.")
        print("3. Departamentos.")
        print("4. Ubicaciones.")
        print("otro. Salir.")
        print()
        op0 = int(input("--> "))
        print()
        print("Solo valores numericos.")
        print()
        if op0 == 1:
            print("¿Desea filtrar por nombre?")
            print()
            op1 = str(input("s/n --> "))
            print()
            if op1 == "s" or op1 == "S":
                print("Escriba el nombre:")
                print()
                nombre = str(input("--> "))
                print()
                sql = f"SELECT * FROM employees WHERE first_name = '{nombre}'"
                hoja.execute(sql)
                resultados = hoja.fetchall()
                print("Resultados encontrados:")
                print()
                for fila in resultados:
                    print(fila)
                print()
                input("... ")
                print()
            elif op1 == "n" or op1 == "N":
                sql = f"SELECT * FROM employees"
                hoja.execute(sql)
                resultados = hoja.fetchall()
                print("Resultados encontrados:")
                print()
                for fila in resultados:
                    print(fila)
                print()
                input("... ")
                print()
            else:
                print("No se encuentra entre las opciones...")
                print()
                input("... ")
                print()


                
        if op0 == 2:
            print("¿Desea filtrar por nombre?")
            print()
            op1 = str(input("s/n --> "))
            print()
            if op1 == "s" or op1 == "S":
                print("Escriba el nombre:")
                print()
                nombre = str(input("--> "))
                print()
                sql = f"SELECT * FROM employees WHERE first_name = '{nombre}'"
                hoja.execute(sql)
                resultados = hoja.fetchall()
                print("Resultados encontrados:")
                print()
                for fila in resultados:
                    print(fila)
                print()
                input("... ")
                print()
            elif op1 == "n" or op1 == "N":
                sql = f"SELECT * FROM employees"
                hoja.execute(sql)
                resultados = hoja.fetchall()
                print("Resultados encontrados:")
                print()
                for fila in resultados:
                    print(fila)
                print()
                input("... ")
                print()
            else:
                print("No se encuentra entre las opciones...")
                print()
                input("... ")
                print()
        else:
            contador = False