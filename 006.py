#! /usr/bin/env python

if __name__ == "__main__":
    print sum(xrange(1, 100 + 1)) ** 2 - \
            sum(x ** 2 for x in xrange(1, 100 + 1))
