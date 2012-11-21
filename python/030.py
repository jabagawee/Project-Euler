print sum([x for x in xrange(2, 1000000) if sum(map(lambda x: x**5, map(int, str(x))))== x])
