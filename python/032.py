from itertools import permutations

p = permutations('123456789')
ans = set()

for permutation in p:
    for mult_pos in xrange(1, 9):
        for equal_pos in xrange(mult_pos+1, 9):
            mult1, mult2, prod = int(''.join(permutation[:mult_pos])), int(''.join(permutation[mult_pos:equal_pos])), int(''.join(permutation[equal_pos:]))
            if mult1 * mult2 == prod:
                ans.add(prod)

print sum(ans)
