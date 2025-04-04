import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time


#slow
from algorithms.bubble_sort import bubble_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.selection_sort import selection_sort

#fast
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


def main():

    slow = {
        'bubble_sort': bubble_sort,
        'insertion_sort': insertion_sort,
        'selection_sort': selection_sort
    }


    fast = {
        'quicksort': quicksort,
        'heap_sort': heap_sort,
        'merge_sort': merge_sort
    }



    random_numbers = read_dataset('datasets/random/100k.txt')


    start_time = time.perf_counter()
    bubble_sort(random_numbers)
    end_time = time.perf_counter()
    print(f"Time taken: {end_time - start_time:.6f} seconds")


if __name__ == '__main__':
    main()