class VerificadorPlanaridade:
    def __init__(self, grafo):
        self.grafo = grafo
        self.vertices = list(grafo.keys())
        self.num_vertices = len(self.vertices)
        self.visitado = [False] * self.num_vertices
        self.pai = [-1] * self.num_vertices
        self.low = [0] * self.num_vertices
        self.profundidade = [0] * self.num_vertices
        self.pontos_articulacao = set()
        self.componentes_biconectados = []
        self.pilha = []
        self.tempo = 0

    def e_planar(self):
        if self.num_vertices < 5:
            return True

        num_arestas = sum(len(vizinhos) for vizinhos in self.grafo.values()) // 2
        if num_arestas > 3 * self.num_vertices - 6:
            return False

        self.encontrar_componentes_biconectados()
        for componente in self.componentes_biconectados:
            if not self.verificar_planaridade_biconectado(componente):
                return False
        return True

    def encontrar_componentes_biconectados(self):
        for i in range(self.num_vertices):
            if not self.visitado[i]:
                self.busca_profundidade_biconectado(i)

    def busca_profundidade_biconectado(self, u):
        self.visitado[u] = True
        self.low[u] = self.profundidade[u] = self.tempo
        self.tempo += 1
        filhos = 0

        for v in self.grafo[self.vertices[u]]:
            indice_v = self.vertices.index(v)
            if not self.visitado[indice_v]:
                self.pai[indice_v] = u
                self.pilha.append((u, indice_v))
                filhos += 1
                self.busca_profundidade_biconectado(indice_v)
                self.low[u] = min(self.low[u], self.low[indice_v])
                if (self.pai[u] == -1 and filhos > 1) or (
                        self.pai[u] != -1 and self.low[indice_v] >= self.profundidade[u]):
                    self.pontos_articulacao.add(u)
                    componente = []
                    while True:
                        aresta = self.pilha.pop()
                        componente.append(aresta)
                        if aresta == (u, indice_v):
                            break
                    self.componentes_biconectados.append(componente)
            elif indice_v != self.pai[u] and self.profundidade[indice_v] < self.profundidade[u]:
                self.low[u] = min(self.low[u], self.profundidade[indice_v])
                self.pilha.append((u, indice_v))

        if self.pai[u] == -1 and self.pilha:
            componente = []
            while self.pilha:
                aresta = self.pilha.pop()
                componente.append(aresta)
            if componente:
                self.componentes_biconectados.append(componente)

    def verificar_planaridade_biconectado(self, componente):
        num_arestas = len(componente)
        num_vertices = len(set(v for aresta in componente for v in aresta))
        return num_arestas <= 2 * num_vertices - 4

#Exemplos de Uso:
def criar_grafo(arestas):
    grafo = {}
    for u, v in arestas:
        if u not in grafo:
            grafo[u] = []
        if v not in grafo:
            grafo[v] = []
        grafo[u].append(v)
        grafo[v].append(u)
    return grafo

arestas_planar = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
grafo_planar = criar_grafo(arestas_planar)
verificador = VerificadorPlanaridade(grafo_planar)
print(f"Grafo planar (K4): {verificador.e_planar()}")

arestas_k5 = [(0, 1), (0, 2), (0, 3), (0, 4),
              (1, 2), (1, 3), (1, 4),
              (2, 3), (2, 4),
              (3, 4)]
grafo_k5 = criar_grafo(arestas_k5)
verificador = VerificadorPlanaridade(grafo_k5)
print(f"Grafo não planar (K5): {verificador.e_planar()}")
