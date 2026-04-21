
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación (+, -, *, /): ")

if operacion == "+":
    print("Resultado:", numero1 + numero2)
elif operacion == "-":
    print("Resultado:", numero1 - numero2)
elif operacion == "*":
    print("Resultado:", numero1 * numero2)
elif operacion == "/":
    if numero2 != 0:
        print("Resultado:", numero1 / numero2)
    else:
        print("Error: no se puede dividir entre cero")
else:
    print("Operación inválida")