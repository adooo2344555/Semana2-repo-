Algoritmo mayorMenor
	
	Definir numero1, numero2 Como Entero
	
	Escribir "Ingrese el primer numero:"
	Leer numero1
	
	Escribir "Ingrese el segundo numero:"
	Leer numero2
	
	Si numero1 > numero2 Entonces
		Escribir numero1, " es mayor"
		Escribir numero2, " es menor"
	SiNo
		Si numero1 < numero2 Entonces
			Escribir numero2, " es mayor"
			Escribir numero1, " es menor"
		SiNo
			Escribir "Los numeros son iguales"
		FinSi
	FinSi
	
FinAlgoritmo