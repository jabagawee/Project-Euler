#! /usr/bin/env python

from util import lcm

if __name__ == "__main__":
    print reduce(lcm, xrange(1, 20 + 1))
