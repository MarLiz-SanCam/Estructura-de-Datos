# Programa que imprime un cuadrado latino de orden N.
#================================
N = int(input("Ingrese el Orden del Cuadrado : "))
nInicial = 1
#================================
arreglo = []
nInicialF = nInicial
for fil in range(0, N):
    aAux = []
    nInicialC = nInicialF
    for col in range(0, N):
        aAux.append(nInicialC)
        nInicialC += 1
        if (nInicialC > N):
             nInicialC = 1
    arreglo.append(aAux)
    nInicialF += 1
    if (nInicialF > N):
        nInicialF = 1
#================================
print()
for fil in range(0, N):
    for col in range(0, N):
        print(arreglo[fil][col], end=" ")
    print()
#================================