"""
Algorytmy sortowania topologicznego (Kahn) w dwóch reprezentacjach.
"""

def topo_sort_list(adj):
    """
    Sortowanie topologiczne (alg. Kahn) na liście incydencji.
    adj: dict {u: [v1, v2, ...]}
    Zwraca listę wierzchołków w porządku topologicznym.
    """
    n = len(adj)
    indeg = [0] * n
    for u in adj:
        for v in adj[u]:
            indeg[v] += 1
    queue = [u for u in adj if indeg[u] == 0]
    order = []
    while queue:
        u = queue.pop()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                queue.append(v)
    return order


def topo_sort_matrix(mat):
    """
    Sortowanie topologiczne (alg. Kahn) na macierzy sąsiedztwa.
    mat: lista list, mat[u][v] == 1 => krawędź u->v.
    Zwraca listę wierzchołków w porządku topologicznym.
    """
    n = len(mat)
    indeg = [0] * n
    for u in range(n):
        for v in range(n):
            if mat[u][v]:
                indeg[v] += 1
    queue = [u for u in range(n) if indeg[u] == 0]
    order = []
    while queue:
        u = queue.pop()
        order.append(u)
        for v in range(n):
            if mat[u][v]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    queue.append(v)
    return order

