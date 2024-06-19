print("Determinar si un carácter es una vocal")
print("**************************************")

c = input("Ingresa una letra: ")
vocales = ["a","e","i","o","u","A","E","I","O","U"]
if c in vocales:
    print("Es una vocal")
else:
    print("Es consonante")