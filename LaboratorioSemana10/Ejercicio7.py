def transformar_texto(texto, lista_numeros):
    resultado = texto
    
    for numero in lista_numeros:
        if numero == 1:
            resultado = resultado.upper()
        elif numero == 2:
            resultado = resultado.lower()
        elif numero == 3:
            resultado = resultado.capitalize()
        
        print("Paso:", numero, resultado)
    
    return resultado


texto = input("Ingrese un texto: ")
numeros = input("Ingrese números (1,2,3) separados por espacio: ")

lista = list(map(int, numeros.split()))

resultado = transformar_texto(texto, lista)
print("Resultado final:", resultado)