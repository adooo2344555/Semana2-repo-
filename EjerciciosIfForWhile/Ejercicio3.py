
notaEstudiante = int(input("Ingrese una nota del 0 al 10: "))

if notaEstudiante >= 9 and notaEstudiante <= 10:
    print("Excelente")
elif notaEstudiante >= 7 and notaEstudiante <= 8:
    print("Bueno")
elif notaEstudiante == 6:
    print("Aprobado")
elif notaEstudiante >= 0 and notaEstudiante <= 5:
    print("Reprobado")
else:
    print("Nota inválida")