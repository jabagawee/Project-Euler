from itertools import permutations
from util import is_prime

mp = 0

# prime pandigital can only be of length 4 or 7
perms = permutations("1234567")

for p in perms:
    p = ''.join(p)
    if p[-1] in "1357" and is_prime(int(p)):
        mp = max(mp, int(p))

if mp == 0:
    perms = permutations("1234")

    for p in perms:
        p = ''.join(p)
        if p[-1] in "13" and is_prime(int(p)):
            mp = max(mp, int(p))


print mp
