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

