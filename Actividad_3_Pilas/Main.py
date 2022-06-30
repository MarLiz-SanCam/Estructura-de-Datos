# Marina Lizeth Santini Camarena
# Actividad 3
from Pilas import Pila
n: int = 5
Size = n
pila = Pila(Size)


salir = False
opcion: int  = 0

while not salir:
    print("\n")
    print("  -|-|-|-|-|-|-|-|-|-|-|-  Árbol Binario  -|-|-|-|-|-|-|-|-|-|-|-")
    print("  |       Oprima el numero de la opción que desee realizar.     |")
    print("  |    Opción 1 - Agregar datos a la pila                       |")
    print("  |    Opción 2 - Eliminar datos de la pila                     |")
    print("  |    Opción 3 - Saber si la pila está llena o no              |")
    print("  |    Opción 4 - Saber cuantos elementos hay en la pila        |")
    print("  |    Opción 5 - mostrar la pila                               |")
    print("  |    Opción 6 - Salir del programa                            |")
    print("  -|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-")
    
    opcion = int(input())
    if(opcion < 1 or opcion > 6): 
        # Sale del programa porque la opción ingresada es incorrecta
        print(" !! ESTA OPCIÓN ES INEXISTENTE")
        salir = True
        
    elif opcion == 1:
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        # Agregando datos a la pila
        print("Ingrese valor")
        insertado = int(input())
        pila.push(insertado)
        print("Dato ingresado con éxito. (",insertado,")")
        # pila.push(15)
        # pila.push(22)
        # pila.push(25)
        # pila.push(32)
        # pila.push(12)      
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

    elif opcion == 2:
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        pila.pop()
        pila.show()
        print("Nodo eliminado con éxito.")
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

    elif opcion == 3:
        # Saber si la pila está vacia o no
        pila.empty()
        if pila.empty() == True:
            print("Estado: Vacía.")
        else:
            print("Estado: Con elementos.")
        
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

    elif opcion == 4: 
        # Saber cuantos elementos hay en la pila
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        print("Tamaño: %d "%(pila.Size()))
    elif opcion == 5: 
        # Ver la pila    
        # print("Tamaño: %d "%(pila.Size()))
        pila.show()
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

    elif opcion == 6:
        # Salir del programa
        print("Programa cerrado")
        salir = True

        

# 
# print(" ------------------------------------ ")
# # Eliminando datos de la pila
# print("Eliminación de datos de la pila")
#

# # Saber si la pila está llena o no
# print(" ------------------------------------ ")
# pila.empty()
# if pila.empty() == True:
#     print("Estado: Vacía.")
# else:
#     print("Estado: Con elementos.")

# # Saber cuantos elementos hay en la pila
# print(" ------------------------------------ ")
