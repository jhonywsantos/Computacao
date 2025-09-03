def bfs_recursivo(grafo, fila, cores):
    if not fila:
        return

    vertice_atual = fila.pop(0)
    print(f"Visitando: {vertice_atual}, cor atual: {cores[vertice_atual]}")

    for vizinho in grafo[vertice_atual]:
        if cores[vizinho] == 'white':
            cores[vizinho] = 'gray'
            fila.append(vizinho)
            print(f"Vértice {vizinho} descoberto e marcado como cinza.")

    cores[vertice_atual] = 'black'
    print(f"Vértice {vertice_atual} concluído e marcado como preto.")
    bfs_recursivo(grafo, fila, cores)

def busca_em_largura(grafo, inicio):
    cores = {vertice: 'white' for vertice in grafo}
    cores[inicio] = 'gray'
    print(f"Iniciando a BFS a partir do vértice: {inicio}")
    bfs_recursivo(grafo, [inicio], cores)
    return cores

#Exemplo de uso:
grafo = {
    'S': ['R', 'W'],
    'R': ['S', 'V'],
    'V': [],
    'W': ['S', 'T', 'X'],
    'T': ['W', 'U'],
    'U': ['T', 'Y'],
    'X': ['W', 'T', 'Y'],
    'Y': ['U', 'X']
}

resultado = busca_em_largura(grafo, 'S')
print("\nEstados finais dos vértices:")
for vertice, cor in resultado.items():
    print(f"{vertice}: {cor}")
