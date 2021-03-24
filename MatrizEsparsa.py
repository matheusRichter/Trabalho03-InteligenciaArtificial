from NodeMatriz import*

# class to store adjacencies
class MatrizEsparsa:

    # class constructor
    def __init__(self,tamanho):
        self.__tamanho = tamanho
        self.__matrizAdj = [[] for i in range(self.__tamanho)]
        # if self.__tamanho < 1000:
        self.__matrizWarshall = [[False for i in range(self.__tamanho)] for j in range(self.__tamanho)]
        self.__matrizDijkstra = [[None for i in range(self.__tamanho)] for j in range(self.__tamanho)]
        self.caminhos = []
        self.caminhoMaisLongo = []

    # function that adds am adjacencie to a verticie
    def setValue(self, i:int, j:int, peso:float):
        self.__matrizAdj[i].insert(j, NodeMatriz(j, peso))
        if self.__tamanho < 1000:
            self.__matrizWarshall[i][j] = True
            self.__matrizDijkstra[i][j] = peso

    # function that returns the adjacencie of a verticie if it exists
    def getValue(self, i:int, j:int):
        for k in self.__matrizAdj[i]:
            if k.getLable() == j:
                return k
            else: return "Value not found"

    # function that removes an adjacencie
    def removeValue(self, i:int, j:int):
        for k in self.__matrizAdj[i]:
            if k.getLabel() == j:
                self.__matrizAdj[i].remove(k)
        if self.__tamanho < 1000:
            self.__matrizWarshall[i][j] = False
            self.__matrizDijkstra[i][j] = None

    # function that prints all adjacencies
    def imprimir(self):
        adjascencias = []
        for i in range(0, len(self.__matrizAdj)):
            verticie = []
            for j in range(0, len(self.__matrizAdj[i])):
                verticie.append(self.__matrizAdj[i][j].content())
            adjascencias.append(verticie)
        print(adjascencias)

    # function that returns list of strings representing edges
    def lista_de_arestas(self):
        arestas = []
        for i in self.__matrizAdj:
            for j in i:
                arestas.append(f'{self.__matrizAdj.index(i)} {j.getLabel()} {j.getPeso()}')
        
        return arestas

    # function that returns the number of adjacencies in the matrix
    def count(self):
        counter = 0
        for i in self.__matrizAdj:
            for _ in i:
                counter += 1
        return counter

    # function that returns the number of adjacencies of a verticie
    def countEach(self, vertice:int):
        counter = 0
        adjs = []
        for i in self.__matrizAdj[vertice]:
            counter += 1
            adjs.append(i.content())
        return counter, adjs

    # function that returns the weight of an adjacencie
    def getPeso(self, vertice:int, lable:int):
        peso = None
        for i in (self.__matrizAdj[vertice]):
            if i.getLabel() == lable:
                peso = i.getPeso()
        return peso

    def warshall(self):
        matriz = self.__matrizWarshall
        for k in range(len(matriz)):
            for i in range(len(matriz)):
                for j in range(len(matriz[0])):
                    if matriz[i][k] and matriz[k][j]:
                        matriz[i][j] = True

        return matriz

    def printWarshall(self, i=None, j=None):
        if i is None and j is None:
            print(self.warshall())
        else:
            print(self.warshall()[i][j])

    def Dijkstra(self):
        matriz = self.__matrizDijkstra.copy()
        for k in range(len(matriz)):
            for i in range(len(matriz)):
                for j in range(len(matriz[0])):
                        if matriz[i][k] is not None and matriz[k][j] is not None:

                            if matriz[i][j] is None:
                                matriz[i][j] = matriz[i][k] + matriz[k][j]

                            elif matriz[i][k] + matriz[k][j] < matriz[i][j]:
                                matriz[i][j] = matriz[i][k] + matriz[k][j]

                            else:
                                matriz[i][j] = matriz[i][j]

                        else:
                            matriz[i][j] = matriz[i][j]

        return matriz

    def printDijkstra(self, i=None, j=None):
        if i is None and j is None:
            return(self.Dijkstra())
        else:
            return(self.Dijkstra()[i][j])

    def largura(self, fila:list, destino:int, visitados:list = []):

        if fila == []: return []
        else:
            x = fila[0]
            fila.pop(0)

            if x == destino:
                visitados.append(x)
                return visitados

            visitados.append(x)

            for i in self.__matrizAdj[x]:
                if i.getLabel() not in fila and i.getLabel() not in visitados:
                    fila.append(i.getLabel())

        return self.largura(fila,destino,visitados)

    def profundidade(self, origem:int, destino:int, visitados:list = []):

        if origem == destino:
            visitados.append(origem) 
            return visitados

        else:
            if origem not in visitados:
                visitados.append(origem)
                for adjacentes in self.__matrizAdj[origem]:
                    x = self.profundidade(adjacentes.getLabel(), destino, visitados)
                    if x != []:
                        return x

        return []

    def profundidadeLimitada(self, origem:int, destino:int, limite:int, visitados:list = []):

        if origem == destino:
            visitados.append(origem) 
            return visitados

        else:
            if limite == 0:
                visitados.append(origem) 
                return visitados
            if origem not in visitados:
                visitados.append(origem)
                for adjacentes in self.__matrizAdj[origem]:
                    x = self.profundidadeLimitada(adjacentes.getLabel(), destino, limite-1, visitados)
                    if x != []:
                        return x

        return []

    def maiorSaida(self):
        saidas = []
        for i in range(self.__tamanho):
            c = self.countEach(i)
            saidas.append(c)

        return saidas.index(max(saidas)), max(saidas)[0]

    def maiorEntrada(self):
        vertices = [0 for _ in range(len(self.__matrizAdj))]

        for i in range(len(self.__matrizAdj)):
            for j in range(len(self.__matrizAdj[i])):
                vertices[self.__matrizAdj[i][j].getLabel()] += 1
        
        maior = vertices[0]
        for k in vertices:
            if k > maior: maior = k

        return vertices.index(maior), maior

    def maioresSaidas(self):
        maiores = []

        saidas = []
        for i in range(self.__tamanho):
            c = self.countEach(i)
            saidas.append([i,c[0]])

        if len(saidas) < 20:
            for i in range(len(saidas)):
                maiores.append(max(saidas))
                saidas.remove(max(saidas))

        elif len(saidas) >= 20:
            for i in range(20):
                maiores.append(max(saidas))
                saidas.remove(max(saidas))

        return maiores

    def maioresEntradas(self):
        maiores = []

        vertices = [[0,i] for i in range(len(self.__matrizAdj))]
        for i in range(len(self.__matrizAdj)):
            for j in range(len(self.__matrizAdj[i])):
                vertices[self.__matrizAdj[i][j].getLabel()][0] += 1
        
        v = vertices.copy()

        if len(vertices) < 20:
            for _ in range(len(v)):
                maiores.append(max(vertices))
                vertices.remove(max(vertices))

        elif len(vertices) >= 20:
            for _ in range(20):
                maiores.append(max(vertices))
                vertices.remove(max(vertices))

        for i in maiores:
            i.reverse()

        return maiores

    """ 
        As funções printAllPathsUntil() e printAllPaths() são
        usadas para retornar uma lista com todos os vértices
        que estão N arestas distantes um vértice especificado
        como origem.
    """
    def printAllPathsUtil(self, origem, distancia, visited, path, contador=0):
        visited[origem]= True
        path.append(origem) 

        if contador == distancia:
            self.caminhos.append(path.copy())
        else: 
            for i in self.__matrizAdj[origem]: 
                if visited[i.getLabel()]== False:
                    self.printAllPathsUtil(i.getLabel(), distancia, visited, path, contador+1) 
                      
        path.pop() 
        visited[origem] = False
   
    def vertice_N_distante(self, s, d): 
        visited =[False]*(self.__tamanho) 

        path = []
        self.caminhos = []
        self.printAllPathsUtil(s, d, visited, path)

        nodes = []
        for i in self.caminhos:
            if i[len(i)-1] not in nodes:
                nodes.append(i[len(i)-1])
        
        return nodes

    """ 
        Funções para encontrar caminho com maior peso entre dois
        vértices (origem e destino).
    """
    def addAllPathsToList(self, origem, destino, visited, path):
        visited[origem]= True
        path.append(origem)

        if origem == destino:
            self.caminhoMaisLongo.append(path.copy())
        else:
            for i in self.__matrizAdj[origem]:
                if visited[i.getLabel()] == False:
                    self.addAllPathsToList(i.getLabel(), destino, visited, path)

        path.pop()
        visited[origem]= False

    def checkLongestPath(self, origem, destino):
        visited =[False]*(self.__tamanho)
        path = []
        self.caminhoMaisLongo = []
        self.addAllPathsToList(origem, destino, visited, path)

        peso = 0
        caminho = []
        for i in self.caminhoMaisLongo:
            contador = 0
            for j in i:
                for k in self.__matrizAdj[j]:
                    if k.getLabel() in i:
                        contador += k.getPeso()
                        break
            if contador > peso:
                peso = contador
                caminho = i

        return f'caminho = {caminho}, peso = {peso}'

    
    # funções para printar todos os caminhos
    def todosOsCaminhos(self, origem, destino):
        visited =[False]*(self.__tamanho)
        path = []
        self.caminhoMaisLongo = []
        self.addAllPathsToList(origem, destino, visited, path)

        return self.caminhoMaisLongo

    def isCyclicUtil(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True

        for neighbour in self.__matrizAdj[v]:
            if visited[neighbour.getLabel()] == False:
                if self.isCyclicUtil(neighbour.getLabel(), visited, recStack) == True: 
                    return True
            elif recStack[neighbour.getLabel()] == True:
                return True

        recStack[v] = False
        return False
  
    # Returns true if graph is cyclic else false 
    def isCyclic(self): 
        visited = [False] * self.__tamanho 
        recStack = [False] * self.__tamanho
        for node in range(self.__tamanho): 
            if visited[node] == False: 
                if self.isCyclicUtil(node,visited,recStack) == True: 
                    return True
        return False

    """ 
        Funções do algoritmo de Prim
        *********  TDE 4  **********
    """
    def isValidEdge(self, u, v, inMST): 
        if u == v: 
            return False
        if inMST[u] == False and inMST[v] == False: 
            return False
        elif inMST[u] == True and inMST[v] == True: 
            return False
        return True
    
    def primMST(self): 
        inMST = [False] * self.__tamanho
        inMST[0] = True

        edge_count = 0
        mincost = 0
        while edge_count < self.__tamanho - 1: 
            minn = None 
            a = -1
            b = -1
            for i in self.__matrizAdj: 
                for j in i: 
                    if minn == None:
                        if self.isValidEdge(self.__matrizAdj.index(i), j.getLabel(), inMST): 
                            minn = j.getPeso()
                            a = self.__matrizAdj.index(i) 
                            b = j.getLabel()
                    elif j.getPeso() < minn: 
                        if self.isValidEdge(self.__matrizAdj.index(i), j.getLabel(), inMST): 
                            minn = j.getPeso()
                            a = self.__matrizAdj.index(i)
                            b = j.getLabel()
    
            if a != -1 and b != -1: 
                print("Edge %d: (%d, %d) cost: %d" % 
                    (edge_count, a, b, minn)) 
                edge_count += 1
                mincost += minn 
                inMST[b] = inMST[a] = True
    
        print("Minimum cost = %d" % mincost)

    """
        Funções sobre cliques
        Metologia ativa 10-21
    """
    def is_clique(self, vertices):
        for v in vertices:
            adjs = self.countEach(v)
            for a in vertices:
                adjs_a = self.countEach(a)
                if a not in adjs[1] or v not in adjs_a: 
                    return False
        return True

    def clique_maximal(self, clique):
        for v in self.__matrizAdj:
            if self.__matrizAdj.index(v) not in clique:
                c = clique.copy()
                c.append(self.__matrizAdj.index(v))
                if self.is_clique(c):
                    return False
        return True

    """
        Funções de Coeficiente
        de Agrupamento
    """

    def agrupamento_local(self, vertice):
        vizinhos = []
        for i in self.__matrizAdj[vertice]:
            if i.getLabel() not in vizinhos: vizinhos.append(i.getLabel())
        n_vizinhos = len(vizinhos)
        if n_vizinhos > 1:
            return len(self.__matrizAdj[vertice]) / (n_vizinhos * (n_vizinhos-1))
        elif n_vizinhos == 1:
            return len(self.__matrizAdj[vertice])
        return 0

    def agrupamento_medio(self):
        somatorio = 0
        for i in range(self.__tamanho):
            somatorio += self.agrupamento_local(i)
        return (1/self.__tamanho) * somatorio

    def is_euleriano(self):
        vertices_impares = 0
        for i in self.__matrizAdj:
            if len(i) % 2 != 0: vertices_impares += 1
        
        if self.is_conexo() and vertices_impares == 2: return True
        return False

    def is_conexo(self):
        m = self.warshall()
        conexo = True

        for i in m:
            if False in i:
                conexo = False
                break

        return conexo

    # posicionamento = proximidade?
    def centralidade_de_posicionamento(self, vertice):
        if self.is_conexo():
            soma_dist = 0
            for i in range(self.__tamanho):
                soma_dist += self.printDijkstra(vertice,i)
            return 1/soma_dist
        else: return f'Não é possível calcular para grafos não conexos'

    def geodesico(self, i, j):
        caminhos = self.todosOsCaminhos(i,j)
        vertices = []
        peso = None
        for caminho in caminhos:
            cont = 0
            for p in range(len(caminho)):
                if p < len(caminho)-1:
                    cont += self.getPeso(p, p+1)
            
            if peso == None: peso = cont
            elif cont < peso: 
                peso = cont
                vertices = caminho
        
        return vertices

    def centralidade_de_intermediacao(self, vertice):
        if self.is_conexo():
            n_geod = 0
            for i in range(self.__tamanho):
                for j in range(self.__tamanho):
                    caminho = self.geodesico(i,j)
                    if vertice in caminho:
                        n_geod += 1
            return n_geod/((self.__tamanho-1)*(self.__tamanho-2))
        return f'Não é possível calcular para grafos não conexos'
