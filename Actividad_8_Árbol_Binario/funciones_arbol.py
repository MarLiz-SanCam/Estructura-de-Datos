from multiprocessing.sharedctypes import Value
from nodo import Nodo

class ArbolBinario:
    def __init__(self):
        self.raiz = None
    
    def vacia(self):
        if self.raiz == None:
            return True
        else:
            return False

    def eliminar(self, value, nodo):
        if self.vacia():
            return "No hay nodos para eliminar"
        else:
            if nodo.value == value:
                nodo = None
                print("Nodo eliminado con éxito.")
                return nodo
            elif value < nodo.value:
                self.buscar(nodo.izqu, value)
                nodo = None
                print("Nodo eliminado con éxito.")
                return nodo
            else:
                self.buscar(nodo.dere, value)
                nodo = None
                print("Nodo eliminado con éxito.")
                return nodo

    def agregar(self, value):
        if self.vacia():
            self.raiz = Nodo(value = value)
        else:
            nodo = self.__get_place(value)
            if value < nodo.value:
                nodo.izqu = Nodo(value = value, parent = nodo, es_izqu = True)
            else:
                nodo.dere = Nodo(value = value, parent = nodo, es_dere = True)    

    def __get_place(self, value):
        aux = self.raiz
        while aux is not None:
            temp = aux
            if value < aux.value:
                aux = aux.izqu
            else:
                aux = aux.dere
        return temp
          
    def muestra_en_orden(self, nodo):
        # ( Izquierda - raiz - derecha)
        if nodo:
            self.muestra_en_orden(nodo.izqu)
            print(nodo.value)
            self.muestra_en_orden(nodo.dere)


    def muestra_post_orden(self, nodo):
        # ( izquierda - derecha - raiz)
        if nodo: 
            self.muestra_post_orden(nodo.izqu)
            self.muestra_post_orden(nodo.dere)
            print(nodo.value)

    
    def muestra_pre_orden(self, nodo):
        # ( raiz - izquierda - derecha)
        if nodo:
            print(nodo.value)
            self.muestra_pre_orden(nodo.izqu)
            self.muestra_pre_orden(nodo.dere)
    
    def buscar(self, nodo, value):
        if nodo == None:
            return None
        else:
            if nodo.value == value:
                return nodo
            elif value < nodo.value:
                return self.buscar(nodo.izqu, value)
            else:
                return self.buscar(nodo.dere, value)