from collections import Counter
from util import prime_factorize

final_factors = Counter()
for x in xrange(2, 20+1):
    factors = prime_factorize(x)
    for factor in factors:
        final_factors[factor] = max(final_factors[factor], factors[factor])

print reduce(lambda a, b: a * b, [x**y for x,y in final_factors.iteritems()])
