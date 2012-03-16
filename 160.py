from collections import Counter
from util import prime_factorize

def f(N):
    factors = Counter()
    ans = 1
    x = 2
    while x <= N:
        tmp = prime_factorize(x)
        t = min(tmp[2], tmp[5])
        tmp -= Counter({2: t, 5: t})
        factors += tmp
        x += 1
    t = min(factors[2], factors[5])
    factors -= Counter({2: t, 5: t})
    for x, y in factors.items():
        ans *= x**y
        ans %= 10**5
    return ans

print f(1000000000000)
