Algoritmo dividirHastaMenorQueUno
    
    Definir numero, divisor Como Real
    Definir contador Como Entero
    
    contador <- 0
    
    Escribir "Ingrese un numero mayor o igual a 1"
    Leer numero
    
    Escribir "Ingrese un divisor mayor que 1"
    Leer divisor
    
    Si numero < 1 O divisor <= 1 Entonces
        Escribir "Datos incorrectos"
    SiNo
		
        Repetir
            numero <- numero / divisor
            contador <- contador + 1
            Escribir "Resultado: ", numero
        Hasta Que numero < 1
        
        Escribir "Total de divisiones realizadas: ", contador
        
    FinSi
    
FinAlgoritmo