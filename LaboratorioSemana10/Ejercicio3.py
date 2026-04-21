def transformar_texto(texto, numero):
    if numero == 1:
        print(texto.upper())
    elif numero == 2:
        print(texto.lower())
    elif numero == 3:
        print(texto.capitalize())
    else:
        print("Opción incorrecta")


texto = input("Ingrese un texto: ")
numero = int(input("Ingrese un número (1, 2 o 3): "))

transformar_texto(texto, numero)