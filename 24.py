from itertools import permutations

p = permutations('0123456789')

for x in xrange(1000000-1):
    p.next()

print ''.join(p.next())
