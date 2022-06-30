# Evaluar una expresión aritmética en notación Infija, 
# por ejemplo la expresión (2+3)*(8-6) debe dar como resultado el valor de 10,
# introducida como cadena de caracteres, el programa debe también determinar 
# si la expresión aritmética está escrita de forma correcta y si es así deberá 
# evaluarla correctamente, utilizar la estructura de datos tipo pila. 
    # Respetando la jerarquía de los operadores aritméticos: 
    # Paréntesis ( )
    # Exponenciación ^
    # Multiplicación, división *  /
    # Suma o resta +  -
# LA FOMA SIMPLE, HACIENDO USO DE 'eval()'

expresion_infij: str
resultado: int 
print( "Ingrese a continuación la expresión que desea evaluar")
expresion = input()
# print("Usted ingresó: ",Expresion)
resultado = eval(expresion)
print(expresion," = ",resultado)