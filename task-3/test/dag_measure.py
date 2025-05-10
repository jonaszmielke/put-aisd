"""
Skrypt pomiarowy: mierzy czasy sortowania, rysuje wykres i zapisuje go do folderu test_results.
"""

import sys
import os
# Dodajemy katalog nadrzędny do ścieżki importów, by widzieć graph_utils i topo_sort
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
import matplotlib.pyplot as plt
from graph_utils import generate_dag, to_adj_list, to_adj_matrix
from topo_sort import topo_sort_list, topo_sort_matrix


def measure_times(ns, density=0.6):
    """
    Mierzy czasy sortowania topologicznego dla listy incydencji i macierzy sąsiedztwa.
    Zwraca dwie listy: t_list oraz t_matrix.
    """
    t_list, t_matrix = [], []
    for n in ns:
        edges = generate_dag(n, density)
        # Lista incydencji
        adj = to_adj_list(n, edges)
        start = time.time()
        topo_sort_list(adj)
        t_list.append(time.time() - start)
        # Macierz sąsiedztwa
        mat = to_adj_matrix(n, edges)
        start = time.time()
        topo_sort_matrix(mat)
        t_matrix.append(time.time() - start)
        print(f"n={n}: list={t_list[-1]:.4f}s, matrix={t_matrix[-1]:.4f}s")
    return t_list, t_matrix


if __name__ == "__main__":
    ns = list(range(100, 6100, 100))  # 60 punktów
    t_list, t_matrix = measure_times(ns, density=0.6)

    # Rysowanie wykresu bez markerów, z pogrubionymi liniami
    plt.figure(figsize=(8, 5))
    plt.plot(ns, t_list, label='Lista incydencji', color='green', linewidth=2)
    plt.plot(ns, t_matrix, label='Macierz sąsiedztwa', color='purple', linewidth=2)
    plt.xlabel('Liczba wierzchołków (n)')
    plt.ylabel('Czas wykonania [s]')
    plt.title('Sortowanie topologiczne: t = f(n)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Zapis wykresu do katalogu test_results
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'test_results'))
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'dag_measure.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Wykres zapisano do {output_path}")

    # Wyświetlenie wykresu (opcjonalne)
    plt.show()