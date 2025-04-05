import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time

from save_results import save_results

#fast algoriths
from algorithms.insertion_sort import insertion_sort
from algorithms.selection_sort import selection_sort
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

    algorithms = {
        'insertion_sort': insertion_sort,
        'selection_sort': selection_sort,
        'heap_sort': heap_sort,
        'merge_sort': merge_sort
    }

    results = {
        'insertion_sort': {},
        'selection_sort': {},
        'heap_sort': {},
        'merge_sort': {}
    }

    i = 1
    datatypes = ["random", "ascending", "descending", "fixed", "v-shaped", "a-shaped"]
    amount = '1m'
    test_start = time.perf_counter()

    for algorithm_name, algorithm in algorithms:

        for datatype in datatypes:

            numbers = read_dataset(f'datasets/{datatype}/{amount}.txt')
            
            print(f'({i}/{(len(datatypes)*len(algorithms))}) Testing {algorithm_name} with {datatype} dataset')
            time_taken = measure_time(algorithm, numbers)
            print(f'Sorted in {time_taken:.6f} seconds\n\n')

            results[algorithm_name][datatype] = time_taken
            i += 1
        

    test_end = time.perf_counter()
    print(f'Testing complete in {test_end - test_start:.6f} seconds\nSaving the results!')
    
    for algorithm_name, result in results:
        save_results(result, f'test3/{algorithm_name}')
    


if __name__ == '__main__':
    main()