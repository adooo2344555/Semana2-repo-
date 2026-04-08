def transformar_palabra(palabra, numero):
    if numero == 1:
        print(palabra.upper())
    elif numero == 2:
        print(palabra.lower())
    elif numero == 3:
        print(palabra.capitalize())
    else:
        print("Opción incorrecta")


palabra = input("Ingrese una palabra: ")
numero = int(input("Ingrese un número (1, 2 o 3): "))

transformar_palabra(palabra, numero)