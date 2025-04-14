def insertion_sort(arr:list):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return


if __name__ == "__main__":
    array = [5, 4, 1, 7, 0, 2, 3, 8]
    print("Unsorted array:")
    print(array)

    insertion_sort(array)

    print("Sorted array:")
    print(array)
