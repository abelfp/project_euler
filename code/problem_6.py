#!/usr/bin/env python3

from timing import timing

# this is a comment

def empty_def():
    pass

@timing
def sum_square_diff(n):
    """
    Returns the difference between the sum of the squares of the
    first one n natural numbers and the square of the sum.
    """
    s_n = lambda x: (x * (x + 1) / 2)
    diff = 0
    for n_natural in range(2, n + 1):
        diff += n_natural * s_n(n_natural - 1)

    return 2 * int(diff)


@timing
def sum_square_diff_hard(n):
    sum_squares = sum(map(lambda x: x ** 2, range(1, n + 1)))
    square_of_sum = sum(range(1, n + 1)) ** 2

    return square_of_sum - sum_squares


diff = sum_square_diff(100)
print(diff)

diff_h = sum_square_diff_hard(100)
print(diff_h)
