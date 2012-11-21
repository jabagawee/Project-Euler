#! /usr/bin/env python

import functools
from math import sqrt
import numpy
import operator


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for x in xrange(3, int(sqrt(n)) + 1, 2):
        if n % x == 0:
            return False
    return True


def prime_generator():
    yield 2
    n = 3
    while True:
        if is_prime(n):
            yield n
        n += 2


def product(seq):
    return reduce(operator.mul, seq)


def factorial(n):
    assert n >= 0
    return product(xrange(1, n + 1)) if n > 1 else 1


def combination(n, r):
    return factorial(n) / factorial(r) / factorial(n - r)

from collections import Counter


def prime_factorize(n):
    if n == 1:
        return Counter({1: 1})
    factors = Counter()
    while n != 1:
        for x in xrange(2, n + 1):
            if n % x == 0:
                factors[x] += 1
                n /= x
                break
    return factors


def proper_divisors(n):
    factors = [(prime, multiplicity)
               for prime, multiplicity in prime_factorize(n).iteritems()]
    f = [0] * len(factors)
    while True:
        yield reduce(operator.mul, (factors[x][0] ** f[x]
                                    for x in xrange(len(factors))), 1)
        i = 0
        while True:
            f[i] += 1
            if f == [factor[1] for factor in factors]:
                return
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i == len(factors):
                return


def d(n):
    return sum(proper_divisors(n))


def sigma_2(n):
    return n ** 2 + sum(x ** 2 for x in proper_divisors(n))


class memoize(object):
   # stolen shamelessly from python.org

    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        try:
            return self.cache[args]
        except KeyError:
            value = self.func(*args)
            self.cache[args] = value
            return value
        except TypeError:
            # uncachable -- for instance, passing a list as an argument.
            # Better to not cache than to blow up entirely.
            return self.func(*args)

    def __repr__(self):
        """Return the function's docstring."""
        return self.func.__doc__

    def __get__(self, obj, objtype):
        """Support instance methods."""
        return functools.partial(self.__call__, obj)


def fib_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def lcm(a, b):
    return abs(a * b) / gcd(a, b)


def phi(n):
    return len([x for x in xrange(1, n) if gcd(x, n) == 1])


def primesfrom2to(n):
    sieve = numpy.ones(n / 3 + (n % 6 == 2), dtype=numpy.bool)
    sieve[0] = False
    for i in xrange(int(n ** 0.5) / 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[((k * k) / 3)::2 * k] = False
            sieve[(k * k + 4 * k - 2 * k * (i & 1)) / 3::2 * k] = False
    return numpy.r_[2, 3, ((3 * numpy.nonzero(sieve)[0] + 1) | 1)]
