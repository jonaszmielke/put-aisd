def heapify(array, n, i):
    """
    Restores the heap property in the subtree with root index i.
    
    :param array: list representing the heap
    :param n: size of the heap (portion of the list to be treated as the heap)
    :param i: index of the root of the subtree
    """
    largest = i       # Assume the element at index i is the largest
    left = 2 * i + 1  # Calculate index of left child
    right = 2 * i + 2 # Calculate index of right child

    # Check if the left child exists and is greater than the current largest
    if left < n and array[left] > array[largest]:
        largest = left

    # Check if the right child exists and is greater than the current largest
    if right < n and array[right] > array[largest]:
        largest = right

    # If the largest element is not the current element, swap and continue heapifying
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)


def heap_sort(array):
    
    n = len(array)

    # 1. Build a max heap from the array
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    # 2. Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        # Move the current root (largest element) to the end of the array
        array[0], array[i] = array[i], array[0]
        # Restore the heap property for the reduced heap
        heapify(array, i, 0)


if __name__ == "__main__":

    array = [5, 4, 1, 7, 0, 2, 3, 8]
    print("Unsorted array:")
    print(array)
    
    heap_sort(array)
    
    print("Sorted array:")
    print(array)
