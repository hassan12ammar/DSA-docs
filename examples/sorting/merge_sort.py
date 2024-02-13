"""
Merge sort is a sorting algorithm that works by dividing an array into smaller subarrays, 
sorting each subarray, and then merging the sorted subarrays back together to form the final sorted array.
T: O(N log N) [AVG, BEST, WORST]
S: O(N)
"""
from collections import deque


def merge(array_1: deque, array_2: deque) -> list:
    result = []
    while array_1 and array_2:
        if array_1[0] < array_2[0]:
            result.append(array_1.popleft())
        else:
            result.append(array_2.popleft())

    # Append any remaining elements
    result.extend(array_1)
    result.extend(array_2)

    return result


def merge_sort(array: list) -> list:
    if len(array) <= 1:
        return array

    middle = len(array) // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])

    return merge(deque(left), deque(right))


if __name__ == "__main__":
    print(merge_sort([]))
    print(merge_sort([5]))
    print(merge_sort([1, 2, 3]))
    print(merge_sort([3, 2, 1]))
    print(merge_sort([1, 7, 5, 17, 2]))
    print(merge_sort([5, 3, 7, 7, 2]))
    print(merge_sort([5, 3, 17, 2]))
