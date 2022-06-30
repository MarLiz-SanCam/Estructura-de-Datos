# Marina Lizeth Santini Camarena
# Actividad 4

from Colas import Cola
n: int = 5
size = n
cola = Cola(size)
dato = int 

salir = False
opcion: int  = 0

while not salir:
    print("\n")
    print("  -|-|-|-|-|-|-|-|-|-|-|-  Árbol Binario  -|-|-|-|-|-|-|-|-|-|-|-")
    print("  |       Oprima el numero de la opción que desee realizar.     |")
    print("  |    Opción 1 - Ingresar datos a la cola.                     |")
    print("  |    Opción 2 - Eliminar un elemento de la cola.              |")
    print("  |    Opción 3 - Saber si la cola está vacía o no.             |")
    print("  |    Opción 4 - Saber cuántos elementos hay en la cola.       |")
    print("  |    Opción 5 - Salir del programa                            |")
    print("  -|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-")
    
    opcion = int(input())
    if(opcion < 1 or opcion > 5): 
        # Sale del programa porque la opción ingresada es incorrecta
        print(" !! ESTA OPCIÓN ES INEXISTENTE")
        salir = True
        #system(clear)

    elif opcion == 1:
        # Ingresar datos a la cola
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        for n in range(0, size):
            print("Ingrese elemento ",n," en la cola: ")
            data = input()
            cola.push(data)
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

    elif opcion == 2:
        # Eliminar dato de la cola
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        cola.pop() # Quitar el primer dato ingresado
        print("dato eliminado con éxito")
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

    elif opcion == 3:
        # Saber si la cola está vacía o no
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        cola.empty()
        if cola.empty() == True:
            print("Estado: Vacía.")
        else:
            print("Estado: Con elementos.")

        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

    elif opcion == 4: 
        # Saber cuántos elementos hay en la cola
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        leng = cola.size
        print("Cantidad de elementos en la cola: ",leng)
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

    elif opcion == 5:
        print("Programa cerrado")
        salir = True
