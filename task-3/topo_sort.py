"""
Topological sorting algorithms (Kahn's) in two representations.
"""

def topo_sort_list(adj):
    """
    Topological sort (Kahn's algorithm) on an adjacency list.
    Returns a list of vertices in topological order.
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
    Topological sort (Kahn's algorithm) on an adjacency matrix.
    Returns a list of vertices in topological order.
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
