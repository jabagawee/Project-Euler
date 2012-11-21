from itertools import permutations

perms = permutations(xrange(1,10+1))

ans = 0

for p in perms:
    if 10 not in (p[1], p[2], p[4], p[6], p[8]) and \
       p[0] < min((p[3], p[5], p[7], p[9])) and \
       p[0] + p[1] + p[2] == p[3] + p[2] + p[4] and \
       p[0] + p[1] + p[2] == p[5] + p[4] + p[6] and \
       p[0] + p[1] + p[2] == p[7] + p[6] + p[8] and \
       p[0] + p[1] + p[2] == p[9] + p[8] + p[1]:
        ans = max(ans, int(''.join(map(str,(p[0], p[1], p[2], p[3], p[2], p[4], p[5], p[4], p[6], p[7], p[6], p[8], p[9], p[8], p[1])))))

print ans
