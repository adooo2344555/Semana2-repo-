Algoritmo divisionNumeros
	
	Definir numero1, numero2 Como Entero
	
	Escribir "Ingrese un numero para dividir"
	Leer numero1
	
	Escribir "Ingrese segundo numero para dividir, no debe ser 0"
	Leer numero2
	
	si numero2 <> 0 Entonces
		total = numero1 / numero2
		Escribir "La division  de los numeros es ", total

	SiNo
		Escribir "Error: No se puede dividir entre 0" 
		
	FinSi
FinAlgoritmo
