def transformar_texto(texto, opcion):
    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto.capitalize()
    else:
        return "Opción inválida"


texto = input("Ingrese un texto: ")

print("--MENÚ --")
print("1. MAYÚSCULAS")
print("2. minúsculas")
print("3. Primera letra mayúscula")
opcion = int(input("Seleccione una opción (1, 2 o 3): "))

resultado = transformar_texto(texto, opcion)
print("Resultado:", resultado)