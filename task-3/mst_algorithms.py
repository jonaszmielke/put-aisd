"""
Algorytm Prima dla Minimalnego Drzewa Rozpinającego w dwóch reprezentacjach.
"""
import heapq
import math

def prim_list(adj):
    """
    Prim na liście incydencji z kopcem priorytetowym.
    adj: {u: [(v, w), ...], ...}
    Zwraca listę krawędzi MST: [(u,v,w), ...]
    Złożoność: O(m log n)
    """
    n = len(adj)
    visited = [False] * n
    mst_edges = []
    # (weight, u, v) – krawędź wychodząca z drzewa
    heap = [(0, 0, 0)]  # start z wierzchołka 0
    while heap and len(mst_edges) < n - 1:
        w, u, v = heapq.heappop(heap)
        if visited[v]:
            continue
        visited[v] = True
        if u != v:
            mst_edges.append((u, v, w))
        for nei, wt in adj[v]:
            if not visited[nei]:
                heapq.heappush(heap, (wt, v, nei))
    return mst_edges


def prim_matrix(mat):
    """
    Prim na macierzy sąsiedztwa bez kopca, O(n^2).
    mat: lista list n×n, 0 jeśli brak krawędzi.
    Zwraca listę krawędzi MST: [(u,v,w), ...]
    """
    n = len(mat)
    in_tree = [False] * n
    key = [math.inf] * n
    parent = [-1] * n
    key[0] = 0
    for _ in range(n):
        # wybierz wierzchołek spoza drzewa z minimalnym kluczem
        u = min((k for k in range(n) if not in_tree[k]), key=lambda x: key[x])
        in_tree[u] = True
        for v in range(n):
            w = mat[u][v]
            if w and not in_tree[v] and w < key[v]:
                key[v] = w
                parent[v] = u
    # zbierz krawędzie
    mst_edges = []
    for v in range(1, n):
        u = parent[v]
        w = mat[u][v]
        mst_edges.append((u, v, w))
    return mst_edges
