print("Calcular el precio cn descuento")
print("-------------------------------")
monto = float(input("Ingresa el monto: "))

if monto > 100:
    descuento = monto * .10
else:
    descuento = monto * .02
    
print(f"El descuento aplicado es: ${descuento}")