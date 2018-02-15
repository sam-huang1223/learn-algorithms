from numpy import array, floor


def binary_search(arr, left_idx, right_idx, target):
    if left_idx > right_idx:
        return 'target not found'

    midpoint = int(floor((left_idx+right_idx)/2))

    if target == arr[midpoint]:
        return midpoint
    elif target < arr[midpoint]:
        right_idx = midpoint - 1
    else:
        left_idx = midpoint + 1

    return binary_search(arr, left_idx, right_idx, target)


sorted_array = array([1,3,4,6,8])
item_index = binary_search(sorted_array, 0, len(sorted_array)-1, target = 6)

print(item_index)
