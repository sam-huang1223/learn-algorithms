from time import clock
from progressbar import ProgressBar


def timeit_1x(original_function):
    def augmented_function(*args, **kwargs):
        startTime = clock()
        output = original_function(*args, **kwargs)
        endTime = clock()
        print('Time elapsed:', endTime - startTime)
        return output

    return augmented_function


def timeit_10000x(original_function):
    def run_10000x(*args, **kwargs):
        pbar = ProgressBar()
        startTime = clock()
        for _ in pbar(range(10000)):
            output = original_function(*args, **kwargs)
        endTime = clock()
        print('Average time elapsed over 10000 runs:', (endTime - startTime)/10000)
        return output

    return run_10000x