from math import sqrt
from util import is_prime

x = 3

while True:
    if not is_prime(x):
        passed = False
        for sq in xrange(1, int(sqrt(x))):
            if is_prime(x-2*sq**2):
                passed = True
        if not passed:
            print x
            break
    x += 2
