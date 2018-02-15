from sorting import RANDOM_ARRAY
from numpy.random import choice


def quicksort(arr):
    ''' i represents end of <= partition, j represents end of > partition
    worst-case performance: n^2 (naive pivot on sorted array)
    best-case performance: nlogn (pivot always splits array in half)
    average-case performance: nlogn
    '''
    # recursive base case
    if len(arr) <= 1:
        return arr

    pivot_idx = naive_pivot(arr)
    #pivot_idx = random_pivot(arr)

    arr[0], arr[pivot_idx] = arr[pivot_idx], arr[0]
    # swap pivot with first element

    pivot = arr[0]
    # pivot is always first element
    i = 0
    for j in range(1, len(arr)):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i], arr[0] = arr[0], arr[i]
    # swap pivot with last element in less-than partition

    arr[:i] = quicksort(arr[:i])
    arr[i + 1:] = quicksort(arr[i + 1:])
    #np.concatenate((quicksort(arr[:i]), [arr[i]], quicksort(arr[i + 1:])))
    return arr


def naive_pivot(arr):
    ''' naive method of choosing first element as the pivot '''
    return 0


def random_pivot(arr):
    ''' pivot is good if it splits array into similarly-sized halves (i.e. look for the median)
    intuition is that 75-25 split is good enough to achieve nlogn, can get 75-25 split 50% of the time
    '''
    return choice(len(arr))


print(quicksort(RANDOM_ARRAY))