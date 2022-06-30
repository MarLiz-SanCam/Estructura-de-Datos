
class Nodo:
    def __init__(self, value = None, parent = None, es_raiz = False, es_izqu = False, es_dere = False):
        self.value = value
        self.izqu = None
        self.dere = None
        self.parent = parent
        self.es_raiz = es_raiz
        self.es_izqu = es_izqu
        self.es_dere = es_dere