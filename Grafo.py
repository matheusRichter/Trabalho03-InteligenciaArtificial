import time

from MatrizEsparsa import*
from Node import*
import random

class Grafo:

    def __init__(self, tamanho:int):
        self.__tamanho = tamanho
        self.__nos = [None for i in range(self.__tamanho)]
        self.__matriz_adj = MatrizEsparsa(tamanho)

    # function to return number of vertecies
    def getSize(self): return self.__tamanho

    # functions that return list of edges
    def arestas(self): return self.__matriz_adj.lista_de_arestas()

    # function to link vertices
    def criaAdjascencia(self, vertice:int, lable:int, peso:float=1):
        self.__matriz_adj.setValue(vertice, lable, peso)

    # function to unlink vertices
    def removeAdjascencia(self, vertice:int, lable:int):
        self.__matriz_adj.removeValue(vertice, lable)

    # function to print matrix of adjacencies
    def imprimeAdjascencias(self):
        self.__matriz_adj.imprimir()

    # function to set node value in list __nos
    def setInfo(self,i:int,info:str):
        self.__nos[i] = Node(info)

    # function to count number of adjacencies of a vertices
    def adjacentes(self, i:int):
        return self.__matriz_adj.countEach(i)
    
    # function that returns name of nodes in _nos
    def getNodes(self):
        nodes = []
        for i in self.__nos:
            nodes.append(i.getNome())
        return nodes

    # get index
    def getIndex(self,nome):
        c = self.getNodes()
        return c.index(nome)

    # function that returns weight of an adjacencie
    def peso(self, i:int, j:int):
        return self.__matriz_adj.getPeso(i, j)

    def warshall(self):
        return self.__matriz_adj.warshall()

    def printWarshall(self, i=None, j=None):
        self.__matriz_adj.printWarshall(i, j)

    def dijkstra(self):
        return self.__matriz_adj.Dijkstra()

    def printDijkstra(self, i=None, j=None):
        return self.__matriz_adj.printDijkstra(i, j)

    def buscaLargura(self, fila:list, j:int):
        return self.__matriz_adj.largura(fila,j)

    def buscaProfundidade(self, origem:int, destino:int):
        return self.__matriz_adj.profundidade(origem, destino)

    def buscaProfundidadeLimitada(self, origem, destino, limite):
        return self.__matriz_adj.profundidadeLimitada(origem, destino, limite)

    def numeroDeVertices(self):
        return len(self.__nos)

    def maiorEntrada(self):
        return self.__matriz_adj.maiorEntrada()

    def maiorSaida(self):
        return self.__matriz_adj.maiorSaida()

    def maioresSaidas(self):
        return self.__matriz_adj.maioresSaidas()

    def maioresEntradas(self):
        return self.__matriz_adj.maioresEntradas()

    def vertices_N_distante(self,s,d):
        return self.__matriz_adj.vertice_N_distante(s,d)

    def caminhoMaisLongo(self, origem, destino):
        return self.__matriz_adj.checkLongestPath(origem,destino)

    def caminhos(self, origem, destino):
        return self.__matriz_adj.todosOsCaminhos(origem, destino)
