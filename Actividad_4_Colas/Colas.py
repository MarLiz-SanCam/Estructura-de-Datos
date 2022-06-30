# Marina Lizeth Santini Camarena
# Actividad 4

from numpy import size, true_divide


class Cola():

    def __init__(self, size):
        self.cola = []
        self.size = size

    def empty(self): # Saber si la cola está vacía
        if len(self.cola) == 0:
            return True
        else: 
            return False

    def push(self, dato): # Ingresar datos a la cola
        self.cola += [dato]
        # self.size += 1

    def pop(self): # Quitar elementos de la cola 
        if self.empty == True:
            print("La cola ya está vacía")
        else:
            self.cola = [self.cola[i] for i in range(1, self.size)]
            self.size -= 1
    
    def show(self): # Mostrar la cola
        n = self.size -1
        while n > -1:
            print(n, " ->", "[",self.cola[n],"]")
            n -= 1
    
    

