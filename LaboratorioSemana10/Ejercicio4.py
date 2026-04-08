def transf_lista(lista, numero):
    for palabra in lista:
        if numero == 1:
            print(palabra.upper())
        elif numero == 2:
            print(palabra.lower())
        elif numero == 3:
            print(palabra.capitalize())
        else:
            print("Opción incorrecta")


texto = input("Ingrese varias palabras separadas por espacio: ")
numero = int(input("Ingrese un número (1, 2 o 3): "))

lista_palabras = texto.split()

transf_lista(lista_palabras, numero)