#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from timing import timing


def fibonacci_seq(f_0, f_1):
    """Generator for the Fibonacci sequence up to number n"""
    f_nm2 = f_0
    f_nm1 = f_1
    while True:
        f_n = f_nm2 + f_nm1
        yield f_n

        f_nm2 = f_nm1
        f_nm1 = f_n


@timing
def sum_even_f_n(f_max):
    f_seq = fibonacci_seq(1, 2)
    f_sum = 2
    while True:
        f_n = next(f_seq)
        if f_n < f_max:
            if f_n % 2 == 0:
                f_sum += f_n
        else:
            return f_sum


@timing
def calcE():
    x = 1
    y = 1
    sum = 0
    while (x < 4000000):
        sum += (x + y)
        x, y = x + 2 * y, 2 * x + 3 * y
    return sum


f_sum = sum_even_f_n(4 * 1e6)
print(f_sum)

f_other = calcE()
print(f_other)
