#! /usr/bin/env python

if __name__ == "__main__":
    print sum(x for x in xrange(1000) if x % 3 == 0 or x % 5 == 0)
