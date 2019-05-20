import time


def exeTime(func):
    def wrapper(*args, **kwargs):
        start = time.clock()
        res = func(*args, **kwargs)
        end = time.clock()
        elapsed = end - start
        print("%s : %.10f" % (func.__name__, elapsed))
        return res

    return wrapper