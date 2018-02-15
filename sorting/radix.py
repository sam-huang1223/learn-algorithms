from itertools import chain
from numpy import array
from utils import time_functions
from sorting import RANDOM_ARRAY


@time_functions.timeit_1x
def radixsort(arr):
    ''' sort based on value of digits '''
    arr = [str(element) for element in arr]
    max_digits = max([len(element) for element in arr])

    for digit_num in range(1, max_digits + 1):
        storage = [[] for _ in range(10)]
        for element in arr:
            if digit_num > len(element):    storage[0].append(element)
            else:                           storage[int(element[-digit_num])].append(element)
        arr = list(chain(*storage))

    return array(arr, dtype=int)


print(radixsort(RANDOM_ARRAY))
