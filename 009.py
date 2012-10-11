#! /usr/bin/env python

from math import sqrt

if __name__ == "__main__":
    for a in xrange(1, 500):
        for b in xrange(1, 500):
            if sqrt(a ** 2 + b ** 2) + a + b == 1000:
                print int(a * b * sqrt(a ** 2 + b ** 2))
