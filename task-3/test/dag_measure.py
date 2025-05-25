"""
Measurement script: measures topological sort times, plots the chart, and saves it to the test_results folder.
"""

import sys
import os
# Add the parent directory to the import path to access graph_utils and topo_sort
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
import matplotlib.pyplot as plt
from graph_utils import generate_dag, to_adj_list, to_adj_matrix
from topo_sort import topo_sort_list, topo_sort_matrix


def measure_times(ns, density=0.6):
    """
    Measures topological sort times for adjacency list and adjacency matrix representations.
    Returns two lists: t_list and t_matrix.
    """
    t_list, t_matrix = [], []
    for n in ns:
        edges = generate_dag(n, density)
        # Adjacency list
        adj = to_adj_list(n, edges)
        start = time.time()
        topo_sort_list(adj)
        t_list.append(time.time() - start)
        # Adjacency matrix
        mat = to_adj_matrix(n, edges)
        start = time.time()
        topo_sort_matrix(mat)
        t_matrix.append(time.time() - start)
        print(f"n={n}: list={t_list[-1]:.4f}s, matrix={t_matrix[-1]:.4f}s")
    return t_list, t_matrix


if __name__ == "__main__":
    ns = list(range(100, 6100, 100))  # 60 sample points
    t_list, t_matrix = measure_times(ns, density=0.6)

    # Plotting the chart without markers, with bold lines
    plt.figure(figsize=(8, 5))
    plt.plot(ns, t_list, label='Adjacency List', linewidth=2)
    plt.plot(ns, t_matrix, label='Adjacency Matrix', linewidth=2)
    plt.xlabel('Number of vertices (n)')
    plt.ylabel('Execution time [s]')
    plt.title('Topological Sort: t = f(n)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Save the chart to the test_results directory
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'test_results'))
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'dag_measure.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Chart saved to {output_path}")

    # Display the chart (optional)
    plt.show()
