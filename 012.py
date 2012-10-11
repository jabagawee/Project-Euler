#! /usr/bin/env python

from util import prime_factorize, product


def num_factors(n):
    factors = prime_factorize(n)
    if n == 1:
        return 1
    return product(x + 1 for x in factors.values())


def triangles():
    triangle, adder = 0, 1
    while True:
        triangle += adder
        adder += 1
        yield triangle

if __name__ == "__main__":
    t = triangles()
    while True:
        triangle = t.next()
        if num_factors(triangle) > 500:
            print triangle
            break
