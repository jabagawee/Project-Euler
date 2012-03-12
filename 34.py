from util import factorial

print sum([x for x in xrange(3, 1000000) if sum(map(factorial, map(int, str(x)))) == x])
