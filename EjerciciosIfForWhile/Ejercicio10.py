
usuarioRegistrado = "admin"
contrasenaRegistrada = "1234"

while True:
    usuario = input("Ingrese el usuario: ")
    contrasena = input("Ingrese la contraseña: ")

    if usuario == usuarioRegistrado and contrasena == contrasenaRegistrada:
        print("Acceso permitido")
        break
    else:
        print("Acceso denegado, intente de nuevo")