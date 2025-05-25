# AISD Course — Task Solutions

This repository contains four separate assignments from the “Algorithms and Data Structures” course at Poznań University of Technology. Each task lives in its own subfolder (`task-1` through `task-4`) and includes:

* **Code** implementing the required algorithms
* **Scripts** to generate data and measure runtimes
* **Result files** (CSV, PNG) with the raw data and plots

---

## Task 1: Sorting Algorithms Performance

📄 [Task 1 Instructions](https://www.cs.put.poznan.pl/mmachowiak/aisd.php?opcja=sortowanie)

**Summary:**

1. Compare three simple sorts (Bubble, Insertion, Selection) on random integer arrays.
2. Compare three “fast” sorts (Heap, Merge, Quick) on random data.
3. Test four sorts (Insertion, Selection, Heap, Merge) on five types of input (random, sorted, reverse, constant, “V-shaped”).
4. Implement QuickSort with three pivot-selection strategies (rightmost, middle, random) and compare on “A-shaped” input.

**Files:**

```plaintext
task-1/
├── generate_datasets.py     
│   # Generates random integer arrays of varying sizes/types for tests.
│
├── algorithms/              
│   ├── bubble_sort.py        # Simple Bubble Sort
│   ├── insertion_sort.py     # Simple Insertion Sort
│   ├── selection_sort.py     # Simple Selection Sort
│   ├── heap_sort.py          # Heap Sort
│   ├── merge_sort.py         # Merge Sort
│   └── quicksort/            
│       ├── quicksort_right.py   # QuickSort pivot = rightmost element
│       ├── quicksort_middle.py  # QuickSort pivot = middle element
│       └── quicksort_random.py  # QuickSort pivot = random element
│
├── datasets/                
│   # (Empty by default) Generated datasets will be saved here
│
├── test/                     
│   ├── test1.py             # Measure simple sorts (I)
│   ├── test2.py             # Measure fast sorts (II)
│   ├── test3.py             # Measure 4 sorts on 5 input types (III)
│   ├── test4.py             # Compare QuickSort pivot strategies (IV)
│   └── save_results.py      # Utility to save timing data to CSV
│
└── test_results/            
    ├── test1.csv            # Timings for simple sorts
    ├── test2.csv            # Timings for fast sorts
    ├── test3.csv            # Timings for mixed-input sorts
    └── test4.csv            # Timings for QuickSort variants
```

---

## Task 2: Comparison of Singly-Linked List vs. BST/AVL

📄 [Task 2 Instructions](https://www.cs.put.poznan.pl/mmachowiak/aisd.php?opcja=lista_bst)

**Summary:**

1. Build a sorted singly-linked list and a Binary Search Tree (BST) from the same random unique integers; measure creation, search, and deletion times.
2. Convert the BST into a height-balanced AVL tree (via in-order traversal + binary-split) and compare heights across different input sizes.

**Files:**

```plaintext
task-2/
├── generate-random-unique.py  
│   # Generates a sequence of non-repeating random integers.
│
├── one-way-list.cpp          
│   # Implements a sorted singly-linked list with insert, search, delete.
│
├── bst.cpp                   
│   # Implements a binary search tree with insert, search, delete.
│
├── datasets/                 
│   # (Empty) Generated random unique lists will be saved here
│
├── test/                     
│   ├── list_measure.cpp      # Benchmarks list creation/search/deletion
│   ├── bst_measure.cpp       # Benchmarks BST creation/search/deletion
│   ├── avl_measure.cpp       # Builds AVL from BST and measures height
│
└── test_results/            
    ├── lista-results.csv     # Raw timings for list operations
    ├── bst_results.csv       # Raw timings for BST operations
    └── avl_results.csv       # Heights/timings for AVL conversion
```

---

## Task 3: Topological Sort & Minimum Spanning Tree

📄 [Task 3 Instructions](https://www.cs.put.poznan.pl/mmachowiak/aisd.php?opcja=zadanie_3)

**Summary:**
I. Generate random DAGs (60% density) and implement topological sort using both adjacency-list and adjacency-matrix; benchmark vs. number of vertices.
II. Implement a Minimum Spanning Tree algorithm; benchmark on random weighted graphs at 30% and 70% edge densities.

**Files:**

```plaintext
task-3/
├── graph_utils.py            # Graph‐generation utilities (DAG and undirected)
├── topo_sort.py              # Topological sort (list and matrix versions)
├── mst_algorithms.py         # MST algorithm implementation (e.g. Kruskal/Prim)
│
├── test/                     
│   ├── dag_measure.py        # Measures topological sort times
│   └── mst_measure.py        # Measures MST times at 30% & 70% density
│
└── test_results/            
    ├── dag_measure.png       # Plot: t = f(n) for topological sort
    ├── mst_measure_30.png    # Plot: t = f(n) for MST at 30% density
    └── mst_measure_70.png    # Plot: t = f(n) for MST at 70% density
```

---

## Task 4: Eulerian & Hamiltonian Cycles in Graphs

📄 [Task 4 Instructions](https://www.cs.put.poznan.pl/mmachowiak/aisd.php?opcja=zadanie_4)

**Summary:**
I. Generate two undirected graphs (Eulerian & Hamiltonian) at 30% (“sparse”) and 70% (“dense”) edge saturation; implement:

* Algorithm A for finding an Eulerian cycle
* Algorithm B (with backtracking) to find the first Hamiltonian cycle
  Benchmark both over 15 sizes.
  II. For a 50%-saturated Hamiltonian graph, enumerate **all** Hamiltonian cycles (Algorithm B) and plot t = f(n).

**Files:**

```plaintext
task-4/
├── part-1/                  # Task 4 I: Eulerian vs. Hamiltonian cycle timing
│   ├── graph_generator.cpp   # Generates connected Eulerian/Hamiltonian graphs
│   ├── measure.cpp           # Benchmarks Algorithm A & B at 30%/70% density
│   ├── generate_images.py    # (Optional) Plot generation script
│   └── graphs/               # (Empty) Generated graphs will be saved here
│
├── part-2/                  # Task 4 II: Enumerate all Hamiltonian cycles
│   ├── hamilton_50.cpp       # Backtracking to list all cycles on 50%-dense graph
│   └── plot_hamilton_50.py   # Plots t = f(n) from “hamilton_50.csv”
│
└── results/                 
    ├── results_30.csv        # Timings for 30% density (A & B)
    ├── results_70.csv        # Timings for 70% density (A & B)
    ├── plot_30.png           # Plot for 30% density
    ├── plot_70.png           # Plot for 70% density
    ├── hamilton_50.csv       # Raw timings / counts for part II
    └── plot_hamilton_50.png  # Plot for part II
```