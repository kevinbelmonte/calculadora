print ("calculadora basica")

numero1 = float(input("ingresar un numero:"))
numero2 = float(input("ingresar un numero:"))

print("\n--- Resultados ---")
print("suma:", numero1+ +numero2)
print("Resta:", numero1 - numero2)
print("multiplicacion:", numero1 * numero2)

if numero2 != 0:
    print("division", numero1 / numero2)
else:
    print("la division no se puede dividir por cero")
