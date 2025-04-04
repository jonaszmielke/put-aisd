import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time

from save_results import save_results

#fast algoriths
from algorithms.quicksort import quicksort
from algorithms.heap_sort import heap_sort
from algorithms.merge_sort import merge_sort


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

def measure_time(function:function, numbers:list):

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
        'bubble_sort': {},
        'insertion_sort': {},
        'selection_sort': {}
    }

    i = 1
    datasets = list(range(1, 16)) #CHANGE THE NUMBERS !!!!!!!!!
    test_start = time.perf_counter()

    #ammount of thousands numbers in dataset
    for ammount in datasets:

        numbers = read_dataset(f'datasets/random/{ammount}k.txt')

        for algorithm_name, algorithm in fast:

            print(f'({i}/{(len(datasets)*len(fast))}) Sorting {ammount}k numbers using {algorithm_name}')
            time_taken = measure_time(algorithm, numbers)
            print(f'Sorted in {time_taken:.6f} seconds\n\n')

            results[algorithm_name][f'{ammount}k'] = time_taken
        

    test_end = time.perf_counter()
    print(f'Testing complete in {test_end - test_start:.6f} seconds\nSaving the results!')
    save_results(results, 'fast')
    


if __name__ == '__main__':
    main()