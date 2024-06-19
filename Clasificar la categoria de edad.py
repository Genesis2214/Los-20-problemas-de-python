print("Clasificar la categoría de edad")
print("-------------------------------")

categoria1 = input("Ingresa la categoria 1: ")
edad1 = int(input("Ingrese la edad: "))

categoria2 = input("Ingresa la categoria 2: ")
edad2 = int(input("Ingrese la edad: "))

categoria3 = input("Ingresa la categoria 3: ")
edad3 = int(input("Ingrese la edad: "))

if edad1 != edad2 and edad1 != edad3 and edad2 != edad3:
    if edad1 < edad2:
        if edad1 < edad3:
            print(f"{categoria1} tiene la menor edad {edad1}")
        else:
            print(f"{categoria3} tiene la menor edad {edad3}")
    else:
        if edad2 < edad3:
            print(f"{categoria2} tiene la menor edad {edad2}")
        else:
            print(f"{categoria3} tiene la menor edad {edad3}")
else:
    print("Las edades tienen que ser diferentes")