texto = "ING. Brayan.txt"

texto2 = texto.split("ING. ")

texto3 = texto2[1].split(".txt")

texto4 = texto3[0].lower()

print(texto4)