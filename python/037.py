from util import is_prime
from itertools import islice

def truncatable(n):
    if not is_prime(n):
        return False
    for x in xrange(1,len(str(n))):
        if not is_prime(int(str(n)[:x])) or not is_prime(int(str(n)[x:])):
            return False
    return True

def truncatable_gen():
    x = 8
    while True:
        if truncatable(x):
            yield x
        x += 1

print sum(islice(truncatable_gen(), 0, 11))
