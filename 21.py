from util import d

ans = 0

for x in xrange(1, 10000):
    if d(d(x)) == x and d(x) != x:
        ans += x

print ans
