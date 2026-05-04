positivos = 0
negativos = 0

while True:
    num = int(input("Ingrese un número (0 para salir): "))

    if num == 0:
        break

    if num > 0:
        positivos += 1
    else:
        negativos += 1

datos = [positivos, negativos]
nombres = ["Positivos", "Negativos"]

for i in range(2):
    print(nombres[i], ":", datos[i])
