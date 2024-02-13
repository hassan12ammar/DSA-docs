"""
Insertion sort is one of the most basic sorting algorithms that essentially inserts 
an element into the right position of an already sorted list. It is usually added at the end 
of a new array and moves down until it finds an element smaller thank itself (the desired position). 
The process repeats for all the elements in the unsorted array.
T: O(N **2) [AVG, WORST]
   O(N) [BEST]
S: O(1)
"""


def insertion_sort(array: list) -> list:
    for index, number in enumerate(array):
        for index_2, number_2 in enumerate(array[:index]):
            if number < number_2:
                array[index], array[index_2] = array[index_2], array[index]

    return array


if __name__ == "__main__":
    print(insertion_sort([1, 7, 5, 17, 2]))
    print(insertion_sort([5, 3, 7, 7, 2]))
    print(insertion_sort([5, 3, 17, 2]))
