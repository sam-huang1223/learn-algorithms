from memory_profiler import profile

def compare_time(func_1, func_2, inputs, iterations=1):
    """
    :return: func_2 running time compared to func_1 (as a multiplicative factor)
    """
    raise NotImplementedError


def compare_time_2_inputs(func, input_1, input_2, iterations=1):
    """
    :return: running time of input_2 compared to input_1 (as a multiplicative factor
    """
    raise NotImplementedError
