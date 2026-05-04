suma = 0
impares = []

while True:
    num = int(input("Ingrese un número (0 para salir): "))

    if num == 0:
        break

    if num % 2 != 0:
        suma += num
        impares.append(num)

print("Suma:", suma)

for i in impares:
    print("Impar:", i)
