mds = 0

for a in xrange(100):
    for b in xrange(100):
        mds = max(mds, sum(map(int, str(a**b))))

print mds
