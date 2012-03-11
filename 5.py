from collections import Counter

def prime_factorize(n):
    if n == 1:
        return Counter({1: 1})
    factors = Counter()
    while n != 1:
        for x in xrange(2, n+1):
            if n % x == 0:
                factors[x] += 1
                n /= x
                break
    return factors

final_factors = Counter()
for x in xrange(2, 20+1):
    factors = prime_factorize(x)
    for factor in factors:
        final_factors[factor] = max(final_factors[factor], factors[factor])

print reduce(lambda a, b: a * b, [x**y for x,y in final_factors.iteritems()])
