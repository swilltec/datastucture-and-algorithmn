import time


def timeit(func):
    def wrapper(*args, **kwargs):
        starttime = time.time()
        func(*args, **kwargs)
        endtime = time.time()
        print(endtime-starttime)
    return wrapper
