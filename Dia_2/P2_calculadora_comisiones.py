
nombre = input("Bienvenido/a, ingrese su nombre: ")
ventas = float(input("Ingrese el importe de sus ventas: "))

total_ventas = round(ventas*0.13,2)
print(f"Super {nombre} tus ganancias totales son: {total_ventas}")
