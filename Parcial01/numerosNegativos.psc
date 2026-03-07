Algoritmo numerosNegativos
	
	Definir numero, suma Como Entero
	
	suma = 0
	
	Repetir
		Escribir "Ingrese un numero"
		Leer numero
		
		Si numero >= 0 Entonces
			suma = suma + numero
		FinSi
		
	Hasta Que numero < 0
	
	Escribir "La suma de los numeros positivos es: ", suma
	
FinAlgoritmo