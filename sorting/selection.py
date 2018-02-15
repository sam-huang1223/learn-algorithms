"""
(n^2)/2 -> O(N^2) always - running time insensitive to input
Linear memory usage - uses minimal number of exchanges to sort

Invariants: elements left of pointer is sorted, elements to the right are unknown
"""

from sorting import RANDOM_ARRAY
from utils import timing


@timing.timeit_1x
def selection_sort(arr):
    """ensures first i elements are sorted (first i elements are first i minimums of the array)"""
    for i in range(len(arr)):

        print(arr)

        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # 1 exchange per element in the array
    return arr


selection_sort(RANDOM_ARRAY)
