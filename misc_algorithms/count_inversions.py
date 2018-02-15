import numpy as np
from utils import time_functions

np.random.seed(1223)

## TODO make this work based on own mergesort implementation

unsorted_array = [6, 5, 4, 4, 2, 1]

# every inversion is either left, right, or split
# running time is same as merge sort, another divide and conquer algorithm - O(nlogn)

def merge_sort_and_count_inversions(unsorted_array):
    if len(unsorted_array) == 1:
        return unsorted_array, 0

    separator_idx = int(np.floor(len(unsorted_array)/2))
    left = unsorted_array[:separator_idx]
    right = unsorted_array[separator_idx:]

    sorted_left, left_inversions = merge_sort_and_count_inversions(left)
    sorted_right, right_inversions = merge_sort_and_count_inversions(right)
    sorted_array, split_inversions = merge_sort_and_count_split_inversions(sorted_left, sorted_right)

    return sorted_array, (left_inversions + right_inversions + split_inversions)

def merge_sort_and_count_split_inversions(sorted_left, sorted_right):
    left_idx = right_idx = num_inversions = 0
    sorted_array = []

    while left_idx < len(sorted_left) and right_idx < len(sorted_right):
        if sorted_left[left_idx] <= sorted_right[right_idx]:
            sorted_array.append(sorted_left[left_idx])
            left_idx += 1
        else:
            sorted_array.append(sorted_right[right_idx])
            right_idx += 1
            num_inversions += len(sorted_left) - left_idx

    if left_idx == len(sorted_left) or right_idx == len(sorted_right):
        sorted_array.extend(sorted_left[left_idx:] or sorted_right[right_idx:])
        # or statement returns first evaluated value that is not None

    return sorted_array, num_inversions

@time_functions.timeit_1x
def count_inversions(unsorted_arr):
    sorted_arr, num_inversions = merge_sort_and_count_inversions(unsorted_arr)
    print('sorted array', sorted_arr)
    print('inversions: ', num_inversions)

count_inversions(unsorted_array)
