while True:
    num = int(input("Ingrese un número (-1 para salir): "))

    if num == -1:
        break

    for i in range(1, 11):
        resultado = num * i
        if resultado > 20:
            print(num, "x", i, "=", resultado)
