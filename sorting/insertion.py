"""
Continual comparisons to element on the left

Best case: already sorted -> n-1 compares and 0 exchanges
Worst case: reverse sorted -> (n^2)/2 compares and exchanges
Average case: random order -> (n^2)/4 compares and exchanges -> O(N^2)

For partially sorted arrays, insertion sort is O(n) (# exchanges = # inversions)
    Partially sorted: # inversions < cn
    Inversions: a pair of elements that are out of order

Invariants: elements to the left of the pointer are in ascending order, elements to the right are unknown
"""

from sorting import RANDOM_ARRAY
from utils import time_functions


@time_functions.timeit_1x
def insertion_sort(arr):
    """sort that maintains sorted order in first i elements of output"""
    for i in range(1, len(arr)):

        print(arr)

        extracted_value = arr[i]
        j = i - 1
        while j > - 1 and extracted_value < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = extracted_value

    print(arr)

    return arr


insertion_sort(RANDOM_ARRAY)
