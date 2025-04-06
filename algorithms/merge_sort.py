def merge_sort(arr:list):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left:list, right:list):
    result = []
    i = j = 0

    # Merge the two sorted arrays
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

if __name__ == "__main__":
    array = [5, 4, 1, 7, 0, 2, 3, 8]
    print("Unsorted array:")
    print(array)

    sorted_array = merge_sort(array)

    print("Sorted array:")
    print(sorted_array)
