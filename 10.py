from util import is_prime

print sum([x for x in xrange(2000000) if is_prime(x)])
