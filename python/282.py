from util import memoize

@memoize
def A(m, n):
    if m == 0:
        return (n + 1) % 14**8
    if m == 1:
        return (n + 2) % 14**8
    if m == 2:
        return (2 * n + 3) % 14**8
    if m == 3:
        return (2**(n + 3) - 3) % 14**8
    if m > 0 and n == 0:
        return A(m-1, 1)
    if m > 0 and n > 0:
        return A(m-1, A(m, n-1))

ans = 0
for x in xrange(6+1):
    print x
    ans += A(x, x) % 14**8

print ans
