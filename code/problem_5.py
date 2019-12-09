#!/usr/bin/env python3

from fractions import gcd
from functools import reduce

from timing import timing


def scm(a, b):
    return a * b // gcd(a, b)


@timing
def smallest_mult(n_mult):
    """Find the smallest multiple for n_mult integers"""
    return reduce(scm, range(1, n_mult + 1))


print(smallest_mult(20))
