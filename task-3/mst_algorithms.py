import heapq
import math

"""
Prim's algorithm for the Minimum Spanning Tree in two representations.
"""

def prim_list(adj):
    """
    Prim on an adjacency list using a priority queue.
    adj: {u: [(v, w), ...], ...}
    Returns a list of MST edges: [(u, v, w), ...]
    Complexity: O(m log n)
    """
    n = len(adj)
    visited = [False] * n
    mst_edges = []
    # (weight, u, v) – edge outgoing from the tree
    heap = [(0, 0, 0)]  # start from vertex 0
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
    Prim on an adjacency matrix without a heap, O(n^2).
    mat: n x n list of lists, 0 if no edge.
    Returns a list of MST edges: [(u, v, w), ...]
    """
    n = len(mat)
    in_tree = [False] * n
    key = [math.inf] * n
    parent = [-1] * n
    key[0] = 0
    for _ in range(n):
        # select the vertex outside the tree with the minimum key
        u = min((k for k in range(n) if not in_tree[k]), key=lambda x: key[x])
        in_tree[u] = True
        for v in range(n):
            w = mat[u][v]
            if w and not in_tree[v] and w < key[v]:
                key[v] = w
                parent[v] = u
    # collect edges
    mst_edges = []
    for v in range(1, n):
        u = parent[v]
        w = mat[u][v]
        mst_edges.append((u, v, w))
    return mst_edges
