ans = set()

for a in xrange(2, 100+1):
    for b in xrange(2, 100+1):
        ans.add(a**b)

print len(ans)
