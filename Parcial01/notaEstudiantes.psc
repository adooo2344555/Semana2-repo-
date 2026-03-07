Algoritmo notaEstudiantes
	
	Definir numeroNota Como Entero
	
	Repetir
		Escribir "Ingrese la nota (0 a 10): "
		Leer numeroNota
		
		Si numeroNota > 10 O numeroNota < 0 Entonces
			Escribir "Dato incorrecto, ingrese nuevamente"
		FinSi
		
	Hasta Que numeroNota >= 0 Y numeroNota <= 10
	
	
	Si numeroNota >= 6 Entonces
		Escribir "Aprobado"
	SiNo
		Si numeroNota = 5 Entonces
			Escribir "Recuperacion"
		SiNo
			Escribir "Reprobado"
		FinSi
	FinSi
	
FinAlgoritmo