import mpmath

mpmath.mp.dps = 100

nums = ''.join([str(mpmath.mpf(x)**mpmath.mpf('0.5'))[2:] for x in xrange(1, 100+1) if x not in [y**2 for y in xrange(1, 10+1)]])

print sum(map(int, nums))
