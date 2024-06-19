#clasificar  el IMC

print(" 16.Determinar la categoria de un trabajador ")
print("--------------------------------------------- \n")


altura=float(input("Ingrese la altura:"))
peso=float(input("Ingrese el peso :"))
imc = peso/( altura ** 2)

if imc <= 18.5:
    print("Bajo peso")
    
elif 18.5 <= imc <= 24.9:
    print("Normal")
    
elif 25 <= imc <= 29.9:
    print("Sobre peso")
    
elif imc >= 30:
    print("obesidad")
    
else:
    print("obesidad")