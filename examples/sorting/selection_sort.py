"""
Selection sort is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest 
(or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list. 
This process is repeated for the remaining unsorted portion until the entire list is sorted. 
T: O(N **2) [AVG, BEST, WORST]
S: O(1)
"""


def selection_sort(array: list) -> list:
    for index in range(len(array)):
        minimum_index = index
        for index_, number in enumerate(array[index:], start=index):
            if number < array[minimum_index]:
                minimum_index = index_

        array[minimum_index], array[index] = array[index], array[minimum_index]

    return array


if __name__ == "__main__":
    print(selection_sort([1, 7, 5, 17, 2]))
    print(selection_sort([5, 3, 7, 7, 2]))
    print(selection_sort([5, 3, 17, 2]))
