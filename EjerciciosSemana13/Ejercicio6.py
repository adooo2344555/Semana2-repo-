while True:
    n = int(input("Ingrese un número (0 para salir): "))

    if n == 0:
        break

    for num in range(1, n + 1):
        if num > 1:
            es_primo = True

            for i in range(2, num):
                if num % i == 0:
                    es_primo = False

            if es_primo:
                print(num)
