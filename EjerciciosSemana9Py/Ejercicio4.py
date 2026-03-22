# Ejercicio 4

correo = input("Ingrese un correo electrónico: ")

arroba = "@" in correo

if arroba:
    print("El correo es válido")
else:
    print("El correo no es válido")