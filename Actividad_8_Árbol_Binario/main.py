# Programa que permita realizar las siguientes operaciones utilizando expresiones aritméticas: 
#   Crear un árbol binario
#   Insertar un nodo
#   Eliminar un nodo
#   Recorrer el árbol en En-orden
#   Recorrer el árbol en Post-orden
#   Recorrer el árbol en Pre-orden
# ---------------------------------------------------------------------------------------------- #

from funciones_arbol import ArbolBinario

arbol = ArbolBinario()
salir = False
opcion: int  = 0

while not salir:
    print("\n")
    print("  -|-|-|-|-|-|-|-|-|-|-|-  Árbol Binario  -|-|-|-|-|-|-|-|-|-|-|-")
    print("  |       Oprima el numero de la opción que desee realizar.     |")
    print("  |    Opción 1 - Buscar nodo en el arbol.                      |")
    print("  |    Opción 2 - Agregar un nodo al arbol.                     |")
    print("  |    Opción 3 - Eliminar un nodo del arbol.                   |")
    print("  |    Opción 4 - Recorrer el árbol 'In-order'.                 |")
    print("  |    Opción 5 - Recorrer el árbol 'Pre-order'.                |")
    print("  |    Opción 6 - Recorrer el árbol 'Post-order'.               |")
    print("  |    Opción 7 - Salir del programa                            |")
    print("  -|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-")
    
    opcion = int(input())
    if(opcion < 1 or opcion > 7): 
        # Sale del programa porque la opción ingresada es incorrecta
        print(" !! ESTA OPCIÓN ES INEXISTENTE")
        salir = True
        #system(clear)

    elif opcion == 1:
        # Buscar un nodo en el árbol
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        print("BUSCAR UN VALOR EN EL ÁRBOL\n(retorna la derección de memoria donde se encontró, si no se encuentra, retorna 'None')")
        print ("Ingese el valor que desea buscar en el árbol")
        buscado = int(input())
        print(arbol.buscar(arbol.raiz, buscado ))
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

    elif opcion == 2:
        # Agregar un nodo al arbol
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        print("IINGRESAR VALOR AL ÁRBOL")
        agregado = int(input())
        arbol.agregar(agregado)
        print("Nodo agregado con éxito, presione enter para continuar.")
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        input()

    elif opcion == 3:
        # Eliminar un nodo del árbol
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        print(" ELIMINAR UN VALOR DEL ÁRBOL\nIngrese el valor que desea eliminar")
        eliminado = int(input())
        arbol.eliminar(arbol.raiz, eliminado)
        print("Nodo eliminado con éxito.")
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

    elif opcion == 4: 
        # En orden 
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        # ( Izquierda - raiz - derecha)
        # 3, 5, 6, 7, 8, 9, 10, 12, 15
        print("ÁRBOL MOSTRADO 'IN-ORDER'")
        arbol.muestra_en_orden(arbol.raiz)
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

    elif opcion == 5:
        # Pre orden 
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        # ( raiz - izquierda - derecha)
        # 8, 5, 3, 6, 7, 10, 9, 15, 12
        print("ÁRBOL MOSTRADO 'PRE-ORDER'")
        arbol.muestra_pre_orden(arbol.raiz)
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

    elif opcion == 6:
        # Post orden 
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        # ( izquierda - derecha - raiz)
        # 3, 7, 6, 5, 9, 12, 15, 10, 8
        print("ÁRBOL MOSTRADO 'POST-ORDER'")
        arbol.muestra_post_orden(arbol.raiz)
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

    elif opcion == 7:
        print("Programa cerrado")
        salir = True
