from util import memoize

@memoize
def g(k):
    if k >= 0 and k <= 1999:
        return 1
    return g(k-2000) + g(k-1999)

for x in xrange(10000):
    print 'g(%d) = %d' %(x, g(x))

# the above is now legacy code
print 2**(10**18/2000) % 20092010

for x in xrange(10000):
    print '2 ** %d % 20092010 = %d' %(x, 2**x%20092010)
