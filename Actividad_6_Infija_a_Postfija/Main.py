import InfijaPostfija

def convertir(expresion_infija):
    expresion_infija = list(expresion_infija.upper())
    expresion_postfija = []
    return InfijaPostfija.evaluar(expresion_infija, 100, expresion_postfija)

expresion_infija = input("Digite la expresion: ")
print("Expresion Guardada!")

print(convertir(expresion_infija))