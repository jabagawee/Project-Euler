#! /usr/bin/env python

import sys
from util import memoize

sys.setrecursionlimit(10000)


@memoize
def hailstone(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 1 + hailstone(n / 2)
    return 1 + hailstone(3 * n + 1)

if __name__ == "__main__":
    msl = 0  # max sequence length
    ans = 0

    for x in xrange(3, 1000000, 2):
        if hailstone(x) > msl:
            msl = hailstone(x)
            ans = x

    print ans
