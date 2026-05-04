import random

secreto = random.randint(1, 10)
intentos = []

while True:
    num = int(input("Adivina el número (1-10): "))
    intentos.append(num)

    if num == secreto:
        print("¡Correcto!")
        break
    elif num < secreto:
        print("Es mayor")
    else:
        print("Es menor")

for i in intentos:
    print("Intento:", i)
