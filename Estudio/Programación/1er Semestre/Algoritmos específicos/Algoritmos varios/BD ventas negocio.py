def calcular_promedio_ventas():
    # Inicializar los contenedores de datos
    productos = []
    ventas = []
    total_ventas = {}

    # Solicitar datos de entrada al usuario
    num_productos = int(input("Ingrese el número de productos: "))

    for i in range(num_productos):
        producto = input(f"Ingrese el nombre del producto {i+1}: ")
        productos.append(producto)

        venta_mensual = float(input(f"Ingrese la venta mensual del producto {producto}: "))
        ventas.append(venta_mensual)

    # Calcular el promedio de ventas
    total_ventas["Total"] = sum(ventas)
    total_ventas["Promedio"] = sum(ventas) / len(ventas)

    # Imprimir resultados
    print("\nReporte de ventas mensuales")
    print("==========================")
    for producto, venta in zip(productos, ventas):
        print(f"{producto}: ${venta}")

    print("==========================")
    print(f"Total de ventas: ${total_ventas['Total']}")
    print(f"Promedio de ventas: ${total_ventas['Promedio']}")


# Llamar a la función principal
calcular_promedio_ventas()
