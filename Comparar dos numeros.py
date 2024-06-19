print("Determine cuál es mayor o si son iguales")
print("****************************************")

a = int(input("Ingresa un numero: "))
b = int(input("Ingresa un numero: "))

if a == b:
    print("Los numeros son iguales")
else:
    if a > b:
        print(f"El numero mayor es: {a} ")
    else:
        print(f"El numero mayor es: {b} ")