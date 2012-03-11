from math import sqrt

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

from collections import Counter

def prime_factorize(n):
    if n == 1:
        return Counter({1: 1})
    factors = Counter()
    while n != 1:
        for x in xrange(2, n+1):
            if n % x == 0:
                factors[x] += 1
                n /= x
                break
    return factors
