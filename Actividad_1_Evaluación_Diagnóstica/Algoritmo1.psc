Algoritmo Algoritmo1
	Definir  x, z, mayr, menr, i Como Entero
	Escribir "Ingrese dos numeros enteros"
	leer x, z
	
	si x == z Entonces
		Escribir "No se puede realizar el ciclo."
	FinSi
	si x < z Entonces
		menr = x
		mayr = z
	FinSi
	si x > z Entonces
		mayr = x
		menr = z
	FinSi
	Escribir "Asc.  |  Desc."
	para i = menr hasta mayr Hacer
		
		Escribir menr " | " mayr
		menr = menr + 1
		mayr = mayr - 1
	FinPara
FinAlgoritmo
