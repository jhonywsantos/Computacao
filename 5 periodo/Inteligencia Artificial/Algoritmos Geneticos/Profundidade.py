def bProfundidade(grafo: dict[str, list[str]]) -> None:
    tempo = 1
    entrada = {}
    saida = {}
    visitados = set()
    pilha = []

    for vertice in grafo:
        if vertice in visitados:
            continue
        pilha.append((vertice, 'entrada'))

        while pilha:
            atual, estado = pilha.pop()
            if estado == 'entrada':
                if atual not in visitados:
                    visitados.add(atual)
                    entrada[atual] = tempo
                    tempo += 1
                    pilha.append((atual, 'saida'))
                    for vizinho in reversed(grafo[atual]):
                        if vizinho not in visitados:
                            pilha.append((vizinho, 'entrada'))
            elif estado == 'saida':
                saida[atual] = tempo
                tempo += 1

    print("\nTempo de entrada/saída:")
    for v in grafo:
        print(f"{v}: {entrada.get(v, '-')} / {saida.get(v, '-')}")

# Exemplo:
grafo = {
    'A': ['B', 'I'], 'B': ['C'], 'C': ['E', 'F'],
    'D': ['B', 'H'], 'E': ['C', 'D'], 'F': ['G'],
    'G': ['E'], 'H': ['G'], 'I': ['A']
}
bProfundidade(grafo)
