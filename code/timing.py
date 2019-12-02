import time


def timing(func):
    def wrap(*args):
        t_i = time.time()
        ret = func(*args)
        t_f = time.time()
        print("{} took {:.3f} ms".format(func.__name__, (t_f - t_i) * 1000))

        return ret
    return wrap

