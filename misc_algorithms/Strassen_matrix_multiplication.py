import numpy as np
from utils import time_functions

matA = np.array([[1,2,3,4],[5,6,7,8],[4,3,2,1],[8,7,6,5]])
matB = np.array([[8,7,6,5],[4,3,2,1],[5,6,7,8],[1,2,3,4]])


def strassen(matA, matB):
    # ensure matrices are 2^n by 2^n, if not, fill in missing rows/columns with 0s
    ### CODE

    assert matA.shape == matB.shape, 'Matrices have different shapes'
    assert np.log2(len(matA)).is_integer(), '0 padding failed, matrices are not 2^n by 2^n'

    # recursive base case
    if matA.shape == (1, 1):
        return np.array([[matA[0,0] * matB[0,0]]])

    arr_len = len(matA)
    separator = int(np.floor(arr_len/2))

    A = matA[:separator, :separator]
    B = matA[:separator, separator:]
    C = matA[separator:, :separator]
    D = matA[separator:, separator:]
    E = matB[:separator, :separator]
    F = matB[:separator, separator:]
    G = matB[separator:, :separator]
    H = matB[separator:, separator:]

    P1 = strassen(A, F - H)
    P2 = strassen(A + B, H)
    P3 = strassen(C + D, E)
    P4 = strassen(D, G - E)
    P5 = strassen(A + D, E + H)
    P6 = strassen(B - D, G + H)
    P7 = strassen(A - C, E + F)

    return np.concatenate((np.concatenate((P5+P4-P2+P6, P1+P2), axis=1),
                           np.concatenate((P3+P4, P1+P5-P3-P7), axis=1)))


@time_functions.timeit_1x
def strassen_matrix_multiplication(matA, matB):
    return strassen(matA, matB)


@time_functions.timeit_1x
def numpy_matrix_multiplication(matA, matB):
    return np.matmul(matA, matB)


strassen_product = strassen_matrix_multiplication(matA, matB)
print('strassen product:\n', strassen_product)
numpy_product = numpy_matrix_multiplication(matA, matB)
print('numpy product:\n', numpy_product)
