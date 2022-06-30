Algoritmo Suma_digitos_de_2048
	num = 2048
	sw = 0
	cont = 1
	x = num
	DigitSum6 = 0
	Hacer
		num = x
		x = x - 1
		//Escribir "numero: ",num," x: ",x 
		mientras sw = 0 Hacer
			si num > (cont * 10) Entonces
				cont = cont * 10
			SiNo
				sw = 1
			FinSi
		FinMientras
		mientras num > 10
			R = num mod cont
			D = (num - R)/cont
			suma = suma + D
			num = R
			cont = cont / 10
		FinMientras
		suma1 = suma + R
		//Escribir "suma: ", suma1
		si suma1 == 6 Entonces
			DigitSum6 = DigitSum6 + 1
		FinSi
		//Escribir "num: ", num
		num = 0
		R = 0
		D = 0
		cont = 1
		suma = 0
		suma1 = 0
		sw = 0
	Hasta Que ( x == 0) 
	Escribir "Se encontraron: ", DigitSum6, " números cuyos dígitos individuales suman 6"
FinAlgoritmo
