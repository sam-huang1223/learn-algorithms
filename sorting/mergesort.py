from numpy import floor

from sorting import RANDOM_ARRAY


def merge_sort(arr):
    def merge(left, right):
        sorted_array = []
        A_idx = B_idx = 0

        while len(sorted_array) < (len(left) + len(right)):
            if left[A_idx] <= right[B_idx]:
                sorted_array.append(left[A_idx])
                A_idx += 1
            else:
                sorted_array.append(right[B_idx])
                B_idx += 1

            if A_idx == len(left) or B_idx == len(right):
                sorted_array.extend(left[A_idx:] or right[B_idx:])
                break

        return sorted_array

    if len(arr) == 1:
        return arr

    seperator_index = int(floor(len(arr) / 2))
    left = merge_sort(arr[:seperator_index])
    right = merge_sort(arr[seperator_index:])
    return merge(left, right)


print(merge_sort(RANDOM_ARRAY))
