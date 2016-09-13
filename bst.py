# -*- coding: utf-8 -*-

class Node:
    def __init__(self,val):
        self.valor = val
        self.esq = None
        self.dir = None
    def insert(self, novo_val):
        if self.valor == novo_val:
            pass
        elif self.valor > novo_val:
            if self.esq != None:
                return self.esq.insert(novo_val)
            else:
                self.esq=Node(novo_val)
        elif self.valor < novo_val:
            if self.dir != None:
                return self.dir.insert(novo_val)
            else:
                self.dir=Node(novo_val)

    def find(self, search_val):
        if self.valor == search_val:
             return True
        elif self.valor > search_val:
            if self.esq != None:
                return self.esq.find(search_val)
            else:
                 return False
        elif self.valor < search_val:
            if self.dir != None:
                return self.dir.find(search_val)
            else:
                return False

class Tree:
    def __init__(self):
        self.root=None

    def insert(self, val):
        if self.root != None:              #caso não tenha raiz
            return self.root.insert(val) #cria a raiz com o valor inserido
        else:
            self.root = Node(val)

    def find(self,val):
        if self.root != None:
            return self.root.find(val)
        else:
            return False
