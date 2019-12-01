#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#
# problem_1.py - Solution to Problem 1 of Project Euler
#
# 30Nov2019 - Abel Flores Prieto
#

import time


def timing(func):
    def wrap(*args):
        t_i = time.time()
        ret = func(*args)
        t_f = time.time()
        print("{} took {:.3f} ms".format(func.__name__, (t_f - t_i) * 1000))

        return ret
    return wrap


@timing
def brute_force():
    mult_sum = 0
    for n in range(1000):
        if n % 3 == 0 or n % 5 == 0:
            mult_sum += n
    print(mult_sum)
    return mult_sum


@timing
def one_liner():
    mult_sum = sum([n for n in range(1000) if n % 3 == 0 or n % 5 == 0])
    print(mult_sum)
    return mult_sum

if __name__ == "__main__":
    # both take the same time to run
    brute_force()
    one_liner()
