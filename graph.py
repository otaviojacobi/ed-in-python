# -*- coding: utf-8 -*-
from acha_caminho import *

qtdNodo=int(raw_input("Quantos nodos tem seu grafo ?"))
graph={}
for i in range(qtdNodo):
    chave=raw_input("Digite a chave do nodo: ")
    ligados=[]
    new_node='666'
    while new_node!='':
        new_node=raw_input("Digite qual nodo o nodo %s esta ligado: (digite out para sair): "%chave)
        if new_node!='':
            ligados.append(new_node)
    graph[chave]=ligados


for key in graph.keys():
    print key + ':'
    print graph[key]


print "O caminho achado foi:"
a=acha_caminho(graph,'a','b')
print a
