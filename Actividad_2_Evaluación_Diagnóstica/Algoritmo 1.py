# Programa que genere e imprima una matriz unitaria de orden N.
# (una matriz unitaria de orden N es la que tiene N filas y N columnas
# con todos sus componentes a 0, excepto las de su diagonal principal 
# que están a 1).
import numpy as np
print("Ingrese valor para cantidad de filas y columnas. ")
n = int(input())
# print("Usted ingresó: ",n)
matrizUnitaria = []

for i in range(n):
	fila = []
	for j in range(n):
		val = 1 if i==j else 0
		fila.append(val)
	matrizUnitaria.append(fila)

for i in matrizUnitaria:
    print(i)
# print (matrizUnitaria)