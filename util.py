from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    for x in xrange(3, int(sqrt(n)) + 1, 2):
        if n % x == 0:
            return False
    return True
