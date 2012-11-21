from util import phi

n, max_val = 2, 1
for x in xrange(2,1000000+1):
    val = float(x) / phi(x)
    if val > max_val:
        n, max_val = x, val
