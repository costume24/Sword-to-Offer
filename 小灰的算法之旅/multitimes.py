import time


def multitimes(func):
    def wrapper(*args, **kwargs):
        start = time.clock()
        for i in range(10):
            res = func(*args, **kwargs)
        end = time.clock()
        elapsed = end - start
        print("%s : %.10f" % (func.__name__, elapsed / 10))
        return res

    return wrapper