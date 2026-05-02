repetir = "si"

while repetir == "si":

    total = 0
    n = int(input("Cantidad de ventas: "))

    for i in range(n):
        print("Venta", i+1)

        precio = float(input("Precio: "))
        tipo = input("Cliente (A/B): ").upper()

        desc = 0

        match tipo:
            case "A":
                desc = 0.10
            case "B":
                desc = 0.05
            case _:
                desc = 0

        # if
        if desc > 0:
            descuento = precio * desc
            precio = precio - descuento
            print("Descuento:", descuento)
        else:
            print("No hay descuento")

        total = total + precio

    print("Total final:", total)

    repetir = input("Repetir (si/no): ")