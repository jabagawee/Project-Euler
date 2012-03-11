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

import functools

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
