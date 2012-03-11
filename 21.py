from util import proper_divisors

def d(n):
    return sum(proper_divisors(n))

ans = 0

for x in xrange(1, 10000):
    if d(d(x)) == x and d(x) != x:
        ans += x

print ans
