correcta = "1234"
intentos = 0

while True:
    clave = input("Ingrese contraseña: ")

    if clave == correcta:
        print("Acceso permitido")
        break
    else:
        print("Incorrecta")
        intentos += 1

for i in range(intentos):
    print("Intento fallido", i + 1)
