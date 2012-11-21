#! /usr/bin/env python

from util import is_prime

if __name__ == "__main__":
    print sum(x for x in xrange(2000000) if is_prime(x))
