
from Listas import Lista

lista = Lista()


salir = False
opcion: int  = 0

while not salir:
    print("\n")
    print("  -|-|-|-|-|-|-|-|-|-|-|-|-|-  Árbol Binario  -|-|-|-|-|-|-|-|-|-|-|-|-|-")
    print("  |       Oprima el numero de la opción que desee realizar.             |")
    print("  |    Opción 1 - Insertar un elemento en la lista.                     |")
    print("  |    Opción 2 - Eliminar un elemento al principio de la lista         |")
    print("  |    Opción 3 - Eliminar un elemento en cualquier parte de la lista.  |")
    print("  |    Opción 4 - Eliminar un elemento al final de la lista             |")
    print("  |    Opción 5 - Saber si  la lista está vacía/llena.                  |")
    print("  |    Opción 6 - Saber cuántos elementos hay en la lista.              |")
    print("  |    Opción 7 - Salir del programa                                    |")
    print("  -|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-")
    
    opcion = int(input())
    if(opcion < 1 or opcion > 7): 
        # Sale del programa porque la opción ingresada es incorrecta
        print(" !! ESTA OPCIÓN ES INEXISTENTE")
        salir = True

    elif opcion == 1:
        # Insertar Elementos a la lista
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        agregar = int(input())
        lista.add_last(agregar)
        print("Dato agregado con éxito")
        lista.trail()
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

    elif opcion == 2:
        # Eliminar primero
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        lista.remove_first()       
        print("primer elemento eliminado con éxito")
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

    elif opcion == 3:
        # Eliminar cualquier elemento de la lista
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        print("Ingrese elemento a remover:\n")
        remover = int(input())
        lista.remove_any(remove = remover)
        print("Elemento eliminado con éxito")
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

    elif opcion == 4: 
        # Eliminar un elemento al final de la 
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        print("Remover el último elemento en la lista:\n")
        lista.remove_last()
        print("Elemento eliminado con éxito")
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

    elif opcion == 5:
        # Saber si  la lista está vacía/llena
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        lista.state()
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

    elif opcion == 6:
        # Saber cuántos elementos hay en la lista
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        print("No. de elementos: ")
        lista.count_elements()
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

    elif opcion == 7:
        print("Programa cerrado")
        salir = True
