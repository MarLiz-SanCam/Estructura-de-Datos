# Marina Lizeth Santini Camarena
# Actividad 3

from numpy import size

class Pila():

    def __init__(self, size):
        self.lista = []
        self.tope = 0
        self.size = size

    def empty(self): # Muestra True, si la pila está vacía y False si tiene al menos un dato.
        if self.tope == 0:
            return True
        else:
            return False

    def push(self, num): # agrega datos a la pila 
        if self.tope < self.size:
            self.lista += [num]
            self.tope += 1
        else:
            print(" LA PILA YA ESTÁ LLENA ")

    def pop(self): # Quita datos de la pila 
        if self.empty() == True:
            print(" LA PILA YA ESTÁ VACÍA ")
        else:
            self.tope -= 1
            self.lista = [self.lista[x] for x in range(self.tope)]

    def show(self): #Muestra todos los elementos en la pila
        i = self.tope - 1
        while i > -1:
            print(" [%d]  -> %d "%(i, self.lista[i]))
            i -= 1
        
        
    def Size(self): # Muestra el número de elementos en la pila
        return self.tope

