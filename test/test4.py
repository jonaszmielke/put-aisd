import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time

from save_results import save_results

#quicksort algorithms
from algorithms.quicksort.quicksort_right import quicksort_right
from algorithms.quicksort.quicksort_middle import quicksort_middle
from algorithms.quicksort.quicksort_random import quicksort_random

sys.setrecursionlimit(10**6)

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

def measure_time(function:callable, numbers:list):

    start_time = time.perf_counter()
    function(numbers, 0, len(numbers)-1)
    end_time = time.perf_counter()

    return end_time - start_time


def main():

    algorithms = {
        'right': quicksort_right,
        'middle': quicksort_middle,
        'random': quicksort_random
    }

    results = {
        'right': {},
        'middle': {},
        'random': {}
    }

    i = 1
    datasets = ['1k']
    test_start = time.perf_counter()

    for algorithm_name, algorithm in algorithms.items():

        for amount in datasets:

            numbers = read_dataset(f'datasets/a-shaped/{amount}.txt')
            
            print(f'({i}/{(len(datasets)*len(algorithms))}) Testing {algorithm_name} key quicksort with {amount} numbers')
            time_taken = measure_time(algorithm, numbers)
            print(f'Sorted in {time_taken:.6f} seconds\n\n')

            results[algorithm_name][amount] = time_taken
            i += 1
        

    test_end = time.perf_counter()
    print(f'Testing complete in {test_end - test_start:.6f} seconds\nSaving the results!')
    save_results(results, datasets, 'test4')
    

if __name__ == '__main__':
    main()