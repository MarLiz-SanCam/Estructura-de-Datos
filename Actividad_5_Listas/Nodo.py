
from os import remove


class Nodo():

    def __init__(self, data):
        self.data = data
        self.next = None
        self.delete = remove

     
