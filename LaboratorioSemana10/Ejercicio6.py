def transformar_texto(texto, numero):
    if numero == 1:
        resultado = texto.upper()
    elif numero == 2:
        resultado = texto.lower()
    elif numero == 3:
        resultado = texto.capitalize()
    else:
        print("Opción inválida")
        return
    
    print("Texto :", resultado)
    return len(resultado)


texto = input("Ingrese un texto: ")
numero = int(input("Ingrese un número (1, 2 o 3): "))

cantidad = transformar_texto(texto, numero)
print("Cantidad de caracteres:", cantidad)