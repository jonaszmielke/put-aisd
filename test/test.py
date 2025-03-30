import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time

from algorithms.heap_sort import heap_sort



def read_dataset(filepath):
    """
    Reads numbers from the given file (one number per line)
    and returns a list of integers.
    """
    numbers = []
    with open(filepath, "r") as f:
        for line in f:
            numbers.append(int(line.strip()))

    return numbers



random_numbers = read_dataset('datasets/random/10m.txt')


start_time = time.perf_counter()
heap_sort(random_numbers)
end_time = time.perf_counter()
print(f"Time taken: {end_time - start_time:.6f} seconds")

