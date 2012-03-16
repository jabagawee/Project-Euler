from math import sqrt

limit = 10**8
A = [False] * limit

for x in xrange(1, int(sqrt(limit))+1):
    for y in xrange(1, int(sqrt(limit))+1):
        n = 4 * x**2 + y**2
        if n < limit and (n % 12 in (1, 5)):
            A[n] = not A[n]
        n = 3 * x**2 + y**2
        if n < limit and n % 12 == 7:
            A[n] = not A[n]
        n = 3 * x**2 - y**2
        if x > y and n < limit and n % 12 == 11:
            A[n] = not A[n]

for n in xrange(5, int(sqrt(limit))+1):
    if A[n]:
        for k in xrange(n**2, limit, n**2):
            A[k] = False

A[2], A[3] = True, True
print len([x for x in xrange(limit) if A[x]])
