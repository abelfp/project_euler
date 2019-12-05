#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from timing import timing


@timing
def first_try(n_order):
    n_min = 10 ** (n_order - 1)
    n_max = 10 ** n_order - 1
    for num in reversed(range(n_min ** 2, n_max ** 2)):
        if str(num) == str(num)[::-1]:
            for n_0 in reversed(range(n_min, n_max)):
                if num % n_0 == 0:
                    n_1 = int(num / n_0)
                    if n_1 // 10 ** n_order == 0:
                        print(n_0, n_1)
                        print(n_0 * n_1)
                        return num


@timing
def website_solution(n_order):
    n_min = 10 ** (n_order - 1)
    n_max = 10 ** n_order - 1
    largest_pol = 0
    a = n_max
    while a >= n_min:
        if a % 11 == 0:
            b = n_max
            db = 1
        else:
            b = n_max - (n_max % 11)
            db = 11
        while b >= a:
            if a * b <= largest_pol:
                break
            if str(a * b) == str(a * b)[::-1]:
                largest_pol = a * b

            b -= db
        a -= 1

    return largest_pol

print(website_solution(5))
