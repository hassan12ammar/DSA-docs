"""
Heap sort is a comparison-based sorting technique based on Binary Heap data structure. 
It is similar to the selection sort where we first find the minimum element and place 
the minimum element at the beginning. Repeat the same process for the remaining elements.
T: O(N log N) [AVG, BEST, WORST]
S: O(1)
"""

import heapq


def heap_sort(array: list) -> list:
    heapq.heapify(array)

    return [heapq.heappop(array) 
            for _ in range(len(array))]


if __name__ == "__main__":
    print(heap_sort([]))
    print(heap_sort([1]))
    print(heap_sort([1,5]))
    print(heap_sort([1,5,-1]))
    print(heap_sort([1, 7, 5, 17, 2]))
    print(heap_sort([5, 3, 7, 7, 2]))
    print(heap_sort([5, 3, 17, 2]))


"""
from queue import PriorityQueue


def heap_sort(array: list) -> list:
    heap = PriorityQueue()
    for number in array:
        heap.put(number)

    return [heap.get() 
            for _ in range(len(array))]


if __name__ == "__main__":
    print(heap_sort([1, 7, 5, 17, 2]))
    print(heap_sort([5, 3, 7, 7, 2]))
    print(heap_sort([5, 3, 17, 2]))
"""
