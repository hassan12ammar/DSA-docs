"""
QuickSort is a sorting algorithm based on the Divide and Conquer algorithm that picks an element 
as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct 
position in the sorted array.
T: O(N log N) (AVG, BEST)
   O(N^2) (WORST)
S: O(log N) [AVG, BEST]
   O(N) (WORST)
"""


def quick_sort(array: list) -> list:
    if len(array) < 2:
        return array

    pivot_index = len(array) // 2

    left, right = partition(array, array[pivot_index])
    array = quick_sort(left) + [array[pivot_index]] + quick_sort(right)

    return array


def partition(array: list[int], pivot: int) -> tuple[list[int]]:
    left = []
    right = []

    for number in array:
        if number < pivot:
            left.append(number)
        elif number > pivot:
            right.append(number)
    return left, right


if __name__ == "__main__":
    print(quick_sort([1, 7, 5, 17, 2]))
    print(quick_sort([5, 3, 7, 7, 2]))
    print(quick_sort([5, 3, 17, 2]))
