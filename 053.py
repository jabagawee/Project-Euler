from util import combination

ans = 0

for n in xrange(23, 100+1):
    for r in xrange(n+1):
        if combination(n, r) > 1000000:
            ans += 1

print ans
