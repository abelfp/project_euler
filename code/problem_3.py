#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt

from timing import timing


def sieve_eratosthenes(num):
    """Generator of prime numbers for up to num"""
    primes = [True] * (num - 1)
    prime = 2
    while prime * prime <= num:
        if primes[prime - 2]:
            for i in range(2 * prime, num, prime):
                primes[i - 2] = False
        prime += 1

    return [i + 2 for i, prime in enumerate(primes) if prime]


@timing
def biggest_prime_factor(num):
    """Finds and returns the biggest prime factor of num"""
    primes = sieve_eratosthenes(int(sqrt(num)))

    for prime in primes[::-1]:
        if num % prime == 0:
            return prime

    return None


BIG_NUM = 600851475143
print(biggest_prime_factor(BIG_NUM))
