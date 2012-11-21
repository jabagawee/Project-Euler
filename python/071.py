from fractions import Fraction

all_fractions = set()

for d in xrange(2, 1000000+1):
    for n in xrange(1, d):
        all_fractions.add(Fraction(n,d))

all_fractions = sorted(list(all_fractions))
print all_fractions[all_fractions.index(Fraction(3,7))-1]
