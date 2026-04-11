texto1 = "Python2026"

valido = texto1.isalnum()

if valido:
    texto2 = texto1.lower()
    texto3 = texto2.replace("2026", "")
    print(valido)
    print(texto3)