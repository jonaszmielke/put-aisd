import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time

from save_results import save_results

#fast algoriths
from algorithms.quicksort.quicksort_right import quicksort_right as quicksort
from algorithms.heap_sort import heap_sort
from algorithms.merge_sort import merge_sort


sys.setrecursionlimit(10**9)

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

    if function == quicksort:
        start_time = time.perf_counter()
        function(numbers, 0, len(numbers)-1)
        end_time = time.perf_counter()

    else:
        start_time = time.perf_counter()
        function(numbers)
        end_time = time.perf_counter()

    return end_time - start_time


def main():

    fast = {
        'quicksort': quicksort,
        'heap_sort': heap_sort,
        'merge_sort': merge_sort
    }

    results = {
        'quicksort': {},
        'heap_sort': {},
        'merge_sort': {}
    }

    i = 1
    datasets = [f'{i}m' for i in range(1, 16)]
    test_start = time.perf_counter()

    #amount of thousands numbers in dataset
    for amount in datasets:

        for algorithm_name, algorithm in fast.items():

            numbers = read_dataset(f'datasets/random/{amount}.txt')
            
            print(f'({i}/{(len(datasets)*len(fast))}) Sorting {amount} numbers using {algorithm_name}')
            time_taken = measure_time(algorithm, numbers)
            print(f'Sorted in {time_taken:.6f} seconds\n\n')

            results[algorithm_name][f'{amount}'] = time_taken
            i += 1
        

    test_end = time.perf_counter()
    print(f'Testing complete in {test_end - test_start:.6f} seconds\nSaving the results!')
    save_results(results, datasets, 'test2')
    


if __name__ == '__main__':
    main()