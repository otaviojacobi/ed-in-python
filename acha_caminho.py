# -*- coding: utf-8 -*-
def acha_caminho(graph, inicio, fim, caminho=[]): #função "void"

    caminho=caminho+[inicio]
    if inicio==fim:
        return caminho

    if not graph.has_key(inicio):  #caso grafo nao tenha o inicio do caminho
        return None

    for nodo in graph[inicio]:
        if nodo not in caminho:
            novo_caminho=acha_caminho(graph, nodo, fim, caminho)
            if novo_caminho!= None:
                return novo_caminho
    return caminho
