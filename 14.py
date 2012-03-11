import sys

sys.setrecursionlimit(10000)

from util import memoize

@memoize
def hailstone(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 1 + hailstone(n/2)
    return 1 + hailstone(3*n + 1)

msl = 0 # max sequence length
ans = 0

for x in xrange(3, 1000000, 2):
    if hailstone(x) > msl:
        msl = hailstone(x)
        ans = x

print ans
