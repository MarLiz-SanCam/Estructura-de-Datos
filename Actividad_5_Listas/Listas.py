from itertools import count
from Nodo import Nodo

class Lista():
    def __init__(self):
        self.first = None  # Primero
        self.last = None # Ultimo
    
    def state(self): #indica si está vacia o no la lista
        return self.first == None
    
    def add_first(self, data): #agregar al inicio
        if self.state() == True:
            self.first = self.last = Nodo(data)
        else:
            aux = Nodo(data)
            aux.next = self.first
            self.first = aux

    def add_last(self, data): # agregar el último
        if self.state() == True:
            self.first = self.last = Nodo(data)
        else:
            aux = self.last
            self.last = aux.next = Nodo(data)
        
    def trail(self): # recorrer lista
        aux = self.first
        while aux != None:
            print(aux.data)
            aux = aux.next

    def remove_first(self): # Eliminar el primero
        self.first = self.first.next
        

    def remove_last(self): # eliminar el último
        aux = self.first
        while aux.next != self.last:
            aux = aux.next
        aux.next = None
        self.last = aux

    def remove_any(self, remove): # Eliminar un elemento en cualquier parte de la lista
        aux = self.first
        removed = remove
        while aux != None:
            if (removed == aux):
                aux = aux.next
            aux = aux.next

    def count_elements(self): # Saber cuántos elementos hay en la 
        aux = self.first
        x = 0
        while aux != None:
            x = x + 1
            aux = aux.next
        print("No. de elementos: ",x)

