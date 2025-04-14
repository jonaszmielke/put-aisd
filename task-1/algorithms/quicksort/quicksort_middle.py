def quicksort_middle(array: list, start: int, end: int):
    """
    Quicksort implementation choosing the middle element as pivot.
    """
    if start >= end:
        return

    # Choose middle pivot and swap with last element for partitioning
    mid = (start + end) // 2
    array[mid], array[end] = array[end], array[mid]
    
    pivot_index = partition(array, start, end)

    quicksort_middle(array, start, pivot_index - 1)
    quicksort_middle(array, pivot_index + 1, end)


def partition(array: list, start: int, end: int):
    pivot = array[end]
    i = start - 1

    for j in range(start, end):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[end] = array[end], array[i + 1]
    return i + 1
