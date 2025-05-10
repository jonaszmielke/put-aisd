"""
Skrypt pomiarowy dla MST: generuje wykresy dla gęstości 30% i 70%.
"""
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
import numpy as np
import matplotlib.pyplot as plt
from graph_utils import generate_undirected_graph, to_adj_list_undirected, to_adj_matrix_undirected
from mst_algorithms import prim_list, prim_matrix


def measure_mst(ns, density):
    t_list, t_matrix = [], []
    for n in ns:
        edges = generate_undirected_graph(n, density, weight_range=(1, 1000))
        adj = to_adj_list_undirected(n, edges)
        start = time.time()
        prim_list(adj)
        t_list.append(time.time() - start)
        mat = to_adj_matrix_undirected(n, edges)
        start = time.time()
        prim_matrix(mat)
        t_matrix.append(time.time() - start)
        print(f"n={n}, density={density}: list={t_list[-1]:.4f}s, matrix={t_matrix[-1]:.4f}s")
    return t_list, t_matrix

if __name__ == '__main__':
    ns = list(range(100, 6100, 100))  # 60 punktów
    densities = [0.3, 0.7]
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../test_results'))
    os.makedirs(output_dir, exist_ok=True)

    for dens in densities:
        t_list, t_matrix = measure_mst(ns, dens)
        # Wygładzenie przez interpolację
        x_smooth = np.linspace(min(ns), max(ns), 300)
        y_list = np.interp(x_smooth, ns, t_list)
        y_mat = np.interp(x_smooth, ns, t_matrix)
        # Rysowanie
        plt.figure(figsize=(8, 5))
        plt.plot(x_smooth, y_list, label='Lista incydencji', color='green', linewidth=2)
        plt.plot(x_smooth, y_mat, label='Macierz sąsiedztwa', color='purple', linewidth=2)
        plt.xlabel('Liczba wierzchołków (n)')
        plt.ylabel('Czas wykonania [s]')
        plt.title(f'MST (Prim) t = f(n), density={int(dens*100)}%')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        # Zapis
        fname = f'mst_measure_{int(dens*100)}.png'
        path = os.path.join(output_dir, fname)
        plt.savefig(path, dpi=300, bbox_inches='tight')
        print(f'Wykres zapisano: {path}')
        plt.close()
