"""
Tim Sort is a hybrid sorting algorithm derived from merge sort and insertion sort. 
It was designed to perform well on many kinds of real-world data. Tim Sort is the 
default sorting algorithm used by Python’s sorted() and list.sort() functions.
T: O(N log N) [AVG, WORST]
   O(N) [BEST]
S: O(N)
"""
from insertion_sort import insertion_sort


def merge(array_1, array_2):
    result = []
    while array_1 or array_2:
        if array_1 and not array_2:
            result += array_1
            return result
        if array_2 and not array_1:
            result += array_2
            return result

        if array_1[0] < array_2[0]:
            result.append(array_1.pop(0))
        else:
            result.append(array_2.pop(0))

    return result


def tim_sort(array: list, run_size: int = 4) -> list:
    def separate(array):
        if len(array) > run_size:
            mid = len(array) // 2
            array_2 = array[mid:]
            array_1 = array[:mid]

            array_1 = separate(array_1)
            array_2 = separate(array_2)

            array = merge(array_1, array_2)
            return array

        return insertion_sort(array)

    return separate(array)


if __name__ == "__main__":
    print(tim_sort([5, 2, 8, 1, 0, 3, 6, 7, 2, 4, 10, 34]))
    print(tim_sort([1, 7, 5, 17, 2]))
    print(tim_sort([5, 3, 7, 7, 2]))
    print(tim_sort([5, 3, 17, 2]))
    print(tim_sort([5,-1, 3,-2, 17, 2]))
