#! /usr/bin/env python

from util import is_prime

if __name__ == "__main__":
    num = 600851475143

    while not is_prime(num):
        for x in xrange(3, num, 2):
            if num % x == 0:
                num /= x
                break

    print num
