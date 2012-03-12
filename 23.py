from util import d

PERFECT, DEFICIENT, ABUNDANT = 0, -1, 1

def status(n):
    if d(n) == n:
        return PERFECT
    if d(n) < n:
        return DEFICIENT
    if d(n) > n:
        return ABUNDANT

abundant_nums = [x for x in xrange(12, 28123+1) if status(x) == ABUNDANT]

possibles = set()
for x in abundant_nums:
    for y in abundant_nums:
        possibles.add(x + y)

print sum(filter(lambda x: x not in possibles, xrange(24, 28123+1)))
