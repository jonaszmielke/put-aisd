def selection_sort(arr:list):
    n = len(arr)
    
    for i in range(n):
        min_index = i

        # Find the minimum element in the remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return


if __name__ == "__main__":
    array = [5, 4, 1, 7, 0, 2, 3, 8]
    print("Unsorted array:")
    print(array)

    selection_sort(array)

    print("Sorted array:")
    print(array)
