import random

def quicksort_random(array: list, start: int, end: int):
    """
    Quicksort implementation choosing a random element as pivot.
    """
    if start >= end:
        return

    # Choose a random pivot index and swap with the last element for partitioning
    rand_index = random.randint(start, end)
    array[rand_index], array[end] = array[end], array[rand_index]

    pivot_index = partition(array, start, end)

    quicksort_random(array, start, pivot_index - 1)
    quicksort_random(array, pivot_index + 1, end)


def partition(array: list, start: int, end: int):
    pivot = array[end]
    i = start - 1

    for j in range(start, end):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[end] = array[end], array[i + 1]
    return i + 1
