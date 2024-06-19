# Verifica si un nombre es corto , mediano o largo

print(" 19.Verifica si un nombre es corto , mediano o largo ")
print("-----------------------------------------------------\n")


nombre=input("introduzca su nombre:")

n=len(nombre)

if  n > 5:
    
    print(f"nombre largo")

elif 5 < n < 8:
    print(f"nombre mediano")

else:
    print(f"nombre corto")