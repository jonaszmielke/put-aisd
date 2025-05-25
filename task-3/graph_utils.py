import random

"""
Module with functions for graph generation and representation conversion.
"""

# Part 1

def generate_dag(n, density=0.6):
    """
    Generates a random DAG on n vertices with a given edge density.
    Returns a list of edges (u, v) with u < v.
    """
    max_edges = n * (n - 1) // 2
    m = int(density * max_edges)
    all_edges = [(u, v) for u in range(n) for v in range(u + 1, n)]
    return random.sample(all_edges, m)


def to_adj_list(n, edges):
    """
    Converts an edge list to an adjacency list.
    Returns a dict: {vertex: [neighbors...]}
    """
    adj = {i: [] for i in range(n)}
    for u, v in edges:
        adj[u].append(v)
    return adj


def to_adj_matrix(n, edges):
    """
    Converts an edge list to an adjacency matrix.
    Returns an n x n list of lists, with 1 if the edge exists.
    """
    mat = [[0] * n for _ in range(n)]
    for u, v in edges:
        mat[u][v] = 1
    return mat

# Part 2

def generate_undirected_graph(n, density=0.3, weight_range=(1, 1000)):
    """
    Generates a random undirected weighted graph on n vertices with a given edge density.
    density: ratio of the number of edges to the maximum possible: n(n-1)/2.
    weight_range: range of edge weights (inclusive).
    Returns a list of edges: [(u, v, w), ...], u < v.
    """
    max_edges = n * (n - 1) // 2
    m = int(density * max_edges)
    # Generate all possible undirected pairs u < v
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
    Converts an undirected edge list [(u, v, w), ...] to an adjacency list.
    Returns a dict: {vertex: [(neighbor, weight), ...]}
    """
    adj = {i: [] for i in range(n)}
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    return adj


def to_adj_matrix_undirected(n, edges):
    """
    Converts an undirected edge list to an adjacency matrix.
    Returns an n x n list of lists with weights, or 0 where there is no edge.
    """
    mat = [[0] * n for _ in range(n)]
    for u, v, w in edges:
        mat[u][v] = w
        mat[v][u] = w
    return mat
