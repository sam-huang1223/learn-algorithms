from sorting import RANDOM_ARRAY
from utils import time_functions


@time_functions.timeit_1x
def bubble_sort(arr):
    """inverse of insertion sort - maintains sorted order in last i elements of output"""
    for idx in range(len(arr)):

        print(arr)

        for j in range(len(arr) - idx - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print(arr)

    return arr


bubble_sort(RANDOM_ARRAY)
