print("Determinar si un carácter es una letra o un dígito")
print("__________________________________________________")

c = input("Ingrese una caracter: ")
letra = ["a-z","A-Z"]
digito = ["0,9"]
if c in letra:
    print("Es una letra")
else:
    print("Es un digito")