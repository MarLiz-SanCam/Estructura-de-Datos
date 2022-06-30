Algoritmo Algoritmo3
	n = 100
	Dimension  letras[n], anedac[n]
	Escribir "ingresa caracter por caracter, ingresa: * para salir"
	x = 0
	definir char  Como Caracter
	//char = '*'
	Hacer
		x = x + 1
		leer letras[x]
		//Escribir "ingresaste: ", letras[x]
	Mientras Que (letras[x] <> '*')
	n = x - 1
	para i = 1 hasta n Hacer
		anedac[n] = letras[i]
		//Escribir "anedac ", anedac[n], " letras, ", letras[n]
		n = n - 1
		
	FinPara
	n = x - 1
	//Escribir "n= ",n
	i = 1
	para i = 1 hasta n Hacer
		anedac[i] = letras[n]
		//Escribir "anedac ", anedac[i], " letras, ", letras[i]
		n = n-1
		si (anedac[i] == letras[i]) Entonces
			//Escribir "SI es palindromo"
			z = z + 1
			//Escribir "Z:", z
		FinSi
	FinPara
	n = x - 1
	si (z == n ) Entonces
		Escribir "SI es palindromo"
	SiNo
		Escribir "NO es palindromo"
	FinSi
FinAlgoritmo