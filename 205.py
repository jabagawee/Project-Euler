from collections import Counter
from fractions import Fraction

p_prob = Counter()
c_prob = Counter()

pdie = xrange(1, 4+1)
cdie = xrange(1, 6+1)

for a in pdie:
    for b in pdie:
        for c in pdie:
            for d in pdie:
                for e in pdie:
                    for f in pdie:
                        for g in pdie:
                            for h in pdie:
                                for i in pdie:
                                    p_prob[a+b+c+d+e+f+g+h+i] += 1

for a in cdie:
    for b in cdie:
        for c in cdie:
            for d in cdie:
                c_prob[a+b+c+d] += 1

p_total = sum([x[1] for x in p_prob.items()])
c_total = sum([x[1] for x in c_prob.items()])

for dice_sum in p_prob:
    p_prob[dice_sum] = Fraction(p_prob[dice_sum], p_total)

for dice_sum in c_prob:
    c_prob[dice_sum] = Fraction(c_prob[dice_sum], c_total)

ans = Fraction()

for c_val in c_prob:
    prob_win = sum([x[1] for x in p_prob.items() if x[0] > c_val])
    ans += prob_win * c_prob[c_val]

print float(ans)
