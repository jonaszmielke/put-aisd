"""
Moduł z funkcjami do generowania grafu i konwersji reprezentacji.
"""
import random

#part 1
def generate_dag(n, density=0.6):
    """
    Generuje losowy DAG na n wierzchołkach o zadanym nasyceniu krawędziami.
    Zwraca listę krawędzi (u,v) z u < v.
    """
    max_edges = n * (n - 1) // 2
    m = int(density * max_edges)
    all_edges = [(u, v) for u in range(n) for v in range(u + 1, n)]
    return random.sample(all_edges, m)


def to_adj_list(n, edges):
    """
    Konwersja listy krawędzi do listy incydencji.
    Zwraca dict: {vertex: [neighbors...]}
    """
    adj = {i: [] for i in range(n)}
    for u, v in edges:
        adj[u].append(v)
    return adj


def to_adj_matrix(n, edges):
    """
    Konwersja listy krawędzi do macierzy sąsiedztwa.
    Zwraca listę list rozmiaru n×n, 1 jeśli krawędź istnieje.
    """
    mat = [[0] * n for _ in range(n)]
    for u, v in edges:
        mat[u][v] = 1
    return mat


#part 2
def generate_undirected_graph(n, density=0.3, weight_range=(1, 1000)):
    """
    Generuje losowy graf nieskierowany ważony na n wierzchołkach o zadanym nasyceniu krawędziami.
    density: stosunek liczby krawędzi do maksymalnej możliwej: n(n-1)/2.
    weight_range: przedział wag krawędzi (inclusive).
    Zwraca listę krawędzi: [(u,v,w), ...], u < v.
    """
    max_edges = n * (n - 1) // 2
    m = int(density * max_edges)
    # Wygeneruj wszystkie możliwe nieukierunkowane pary u<v
    all_pairs = [(u, v) for u in range(n) for v in range(u + 1, n)]
    chosen = random.sample(all_pairs, m)
    edges = []
    wmin, wmax = weight_range
    for u, v in chosen:
        w = random.randint(wmin, wmax)
        edges.append((u, v, w))
    return edges


def to_adj_list_undirected(n, edges):
    """
    Konwersja listy krawędzi nieskierowanych [(u,v,w),...] do listy incydencji.
    Zwraca dict: {vertex: [(neighbor, weight), ...]}
    """
    adj = {i: [] for i in range(n)}
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    return adj


def to_adj_matrix_undirected(n, edges):
    """
    Konwersja listy krawędzi nieskierowanych do macierzy sąsiedztwa.
    Zwraca listę list n x n z wagami lub 0 gdy krawędzi brak.
    """
    mat = [[0] * n for _ in range(n)]
    for u, v, w in edges:
        mat[u][v] = w
        mat[v][u] = w
    return mat
