"""
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements 
if they are in the wrong order. This algorithm is not suitable for large data sets as its average and 
worst-case time complexity is quite high.
T: O(N **2) [AVG, WORST]
   O(N) [BEST]
S: O(1)
"""


def bubble_sort(array: list) -> list:
    for _ in array:
        for index, _ in enumerate(array[:-1]):
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]

    return array


if __name__ == "__main__":
    print(bubble_sort([1, 7, 5, 17, 2]))
    print(bubble_sort([5, 3, 7, 7, 2]))
    print(bubble_sort([5, 3, 17, 2]))
