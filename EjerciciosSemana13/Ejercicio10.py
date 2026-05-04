suma = 0
numeros = []

while suma <= 100:
    num = int(input("Ingrese número: "))

    if num >= 0:
        suma += num
        numeros.append(num)

print("Suma total:", suma)

for n in numeros:
    print("Número válido:", n)
